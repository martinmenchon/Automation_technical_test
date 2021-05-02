FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["sh","main.sh"]