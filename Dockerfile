FROM python:3.13-slim

WORKDIR /usr/src/app/bot

COPY requirements.txt .
RUN pip install --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
