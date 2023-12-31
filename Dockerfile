FROM python:3.9-slim

RUN apt-get update && apt-get install -y python3-pip && apt-get clean

WORKDIR /usr/src/app/

COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .