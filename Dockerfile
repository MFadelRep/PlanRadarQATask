FROM python:3.10.0


ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r ./requirements.txt
RUN pip3 install python-dotenv




RUN mkdir /app
COPY ./app /app
WORKDIR /app
