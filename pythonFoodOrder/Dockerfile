FROM python:3.10-slim-bookworm

WORKDIR /giorgikelenjeridze

COPY . .

RUN apt-get update && \
    apt-get -y install gcc build-essential python3-dev postgresql-client && \
    pip install -r prod-requirements.txt

COPY ./entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

EXPOSE 5000

CMD ["sh", "./entrypoint.sh"]
