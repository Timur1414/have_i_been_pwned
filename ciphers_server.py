"""
Модуль отдельного проложения, которое принимает запросы через socket, шифрует текст и отдаёт обратно.
"""
import os
import pickle
import socket
from time import sleep
from dotenv import load_dotenv
from ciphers_algorithms.aes import AES
from ciphers_algorithms.rsa import RSA


class Server:
    """
    Server class that handles socket connections, key generation, and message encryption/decryption.
    """
    def __init__(self, host: str = '127.0.0.1', port: int = 8888, buf_size: int = 1024):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.server.bind((self.host, self.port))
        self.server.listen()
        self.buf_size = buf_size
        print('Server Listening')
        self.open_key = None
        self.close_key = None

        self.address = None
        self.connection = None
        self.client_open_key = None

    def accept(self):
        """
        Accepts a connection from a client and performs a handshake to exchange keys.
        """
        self.connection, self.address = self.server.accept()
        self.__handshake()


    def __handshake(self):
        """
        This method performs a handshake with the client to exchange public keys.
        """
        client_open_key = self.connection.recv(self.buf_size)
        self.client_open_key = pickle.loads(client_open_key)

        serialized_open_key = pickle.dumps(self.open_key)
        self.connection.send(serialized_open_key)

    def get_message(self) -> str:
        """
        This method receives a messages (key, initial vector and data) from the client, decrypts it using RSA and AES.
        """
        message = self.__recv_bytes()
        number_key = RSA.decrypt(message, self.close_key)
        bytes_key = number_key.to_bytes((number_key.bit_length() + 7) // 8, 'big')
        client_key = bytes_key.decode('utf-8')
        print(f'key: {client_key}')
        message = self.__recv_bytes()
        number_initialize_vector = RSA.decrypt(message, self.close_key)
        bytes_initialize_vector = number_initialize_vector.to_bytes((number_initialize_vector.bit_length() + 7) // 8,
                                                                    'big')
        client_initialize_vector = bytes_initialize_vector.decode('utf-8')
        data = self.connection.recv(self.buf_size)
        message = data.decode('utf-8')
        decrypted_message = AES.decrypt_message(message, client_key, client_initialize_vector)
        print(f'Client {self.address} sent "{decrypted_message}"')
        return decrypted_message

    def send_message(self, message: str):
        """
        This method encrypts the message using AES and RSA, then sends it to the client.
        """
        key = AES.generate_key()
        bytes_key = key.encode('utf-8')
        number_key = int.from_bytes(bytes_key, 'big')
        initialize_vector = AES.generate_initialization_vector()
        bytes_initialize_vector = initialize_vector.encode('utf-8')
        number_initialize_vector = int.from_bytes(bytes_initialize_vector, 'big')
        encrypted_key = str(RSA.encrypt(number_key, self.client_open_key))
        self.connection.send(encrypted_key.encode('utf-8'))
        sleep(1)
        encrypted_initialize_vector = str(RSA.encrypt(number_initialize_vector, self.client_open_key))
        self.connection.send(encrypted_initialize_vector.encode('utf-8'))
        sleep(1)
        encrypted_message = AES.encrypt_message(message, key, initialize_vector)
        self.connection.send(encrypted_message.encode('utf-8'))
        sleep(1)

    def close_connection(self):
        """
        This method closes the connection with the client.
        """
        self.connection.close()

    def close_server(self):
        """
        This method closes the server socket.
        """
        self.server.close()

    def generate_keys(self):
        """
        This method generates a pair of RSA keys (public and private) for the server.
        """
        self.open_key, self.close_key = RSA.generate_keys()

    def __recv_bytes(self) -> int:
        """
        This method receives bytes from the client and decodes them to an integer.
        """
        data = self.connection.recv(self.buf_size)
        message = int(data.decode('utf-8'))
        return message


def main():
    load_dotenv()
    server_host = '0.0.0.0'
    server_port = int(os.environ.get('CIPHER_SERVER_PORT', 'Define me!'))
    buf_size = 1024
    server = Server(host=server_host, port=server_port, buf_size=buf_size)
    server.generate_keys()
    end = False
    while not end:
        server.accept()
        try:
            data = server.get_message()
            message = f'text: {data}'
            server.send_message(message)
        except ValueError:
            server.send_message('\0')
        server.close_connection()
    server.close_server()


if __name__ == '__main__':
    main()