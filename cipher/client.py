import pickle
import socket
from time import sleep

from ciphers_algorithms.aes import AES
from ciphers_algorithms.rsa import RSA


class Client:
    def __init__(self, host: str = '127.0.0.1', port: int = 8888, buf_size: int = 1024):
        self.initialize_vector = None
        self.key = None
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
        self.buf_size = buf_size
        self.close_key = None
        self.open_key = None

        self.server_open_key = None

    def connect(self):
        self.client.connect((self.host, self.port))
        self.__handshake()

    def __handshake(self):
        serialized_open_key = pickle.dumps(self.open_key)
        self.client.send((serialized_open_key))

        server_open_key = self.client.recv(self.buf_size)
        self.server_open_key = pickle.loads(server_open_key)

    def __enter_key(self):
        self.key = AES.generate_key()
        bytes_key = self.key.encode('utf-8')
        number_key = int.from_bytes(bytes_key, 'big')
        return number_key

    def __enter_initialize_vector(self):
        self.initialize_vector = 'aaa'
        bytes_initialize_vector = self.initialize_vector.encode('utf-8')
        number_initialize_vector = int.from_bytes(bytes_initialize_vector, 'big')
        return number_initialize_vector

    def send_message(self, message: str):
        number_key = self.__enter_key()
        number_initialize_vector = self.__enter_initialize_vector()
        encrypted_key = str(RSA.encrypt(number_key, self.server_open_key))
        self.client.send(encrypted_key.encode('utf-8'))
        sleep(1)
        encrypted_initialize_vector = str(RSA.encrypt(number_initialize_vector, self.server_open_key))
        self.client.send(encrypted_initialize_vector.encode('utf-8'))
        sleep(1)
        encrypted_message = AES.encrypt_message(message, self.key, self.initialize_vector)
        self.client.send(encrypted_message.encode('utf-8'))
        sleep(1)

    def __recv_bytes(self) -> int:
        data = self.client.recv(self.buf_size)
        message = int(data.decode('utf-8'))
        return message

    def get_message(self) -> str:
        message = self.__recv_bytes()
        number_key = RSA.decrypt(message, self.close_key)
        bytes_key = number_key.to_bytes((number_key.bit_length() + 7) // 8, 'big')
        server_key = bytes_key.decode('utf-8')
        message = self.__recv_bytes()
        number_initialize_vector = RSA.decrypt(message, self.close_key)
        bytes_initialize_vector = number_initialize_vector.to_bytes((number_initialize_vector.bit_length() + 7) // 8,
                                                                    'big')
        server_initialize_vector = bytes_initialize_vector.decode('utf-8')

        data = self.client.recv(self.buf_size)
        message = data.decode('utf-8')
        decrypted_message = AES.decrypt_message(message, server_key, server_initialize_vector)
        print(f'Server sent "{decrypted_message}"')
        return decrypted_message

    def close(self):
        self.client.close()

    def generate_keys(self):
        self.open_key, self.close_key = RSA.generate_keys()
