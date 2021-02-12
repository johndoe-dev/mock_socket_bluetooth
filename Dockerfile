FROM python:slim-buster

COPY . /usr/src/myapp
WORKDIR /usr/src/myapp

ENV HOSTNAME "ipc_server_dns_name"


ENTRYPOINT ["python"]
CMD ["main.py"]