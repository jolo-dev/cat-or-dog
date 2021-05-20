FROM python:3.7-buster

COPY . /home

WORKDIR /home

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]