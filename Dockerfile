FROM python:3.12
LABEL authors="timat"
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y

WORKDIR /have_i_been_pwned

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY cipher ./cipher
COPY ciphers_algorithms ./ciphers_algorithms
COPY have_i_been_pwned ./have_i_been_pwned
COPY main ./main
COPY media ./media
COPY .env .
COPY manage.py .
COPY data.json .

RUN python manage.py migrate
RUN python manage.py loaddata data.json

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
