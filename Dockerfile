FROM python:alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chown root:root ./bin/entrypoint.sh
RUN chmod 4755 ./bin/entrypoint.sh

ENTRYPOINT ["./bin/entrypoint.sh"]