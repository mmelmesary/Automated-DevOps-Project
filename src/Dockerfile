FROM python:3.12.0b4-slim-bullseye AS builder

RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential default-libmysqlclient-dev \
    &&  apt-get install -y pkg-config \
    && pip install --no-cache-dir --upgrade pip

# --no-install-recommends --no-install-suggests : Do not install recommended and suggested packages along with the specified packages. This reduces the amount of disk space used and can speed up the installation process.
# build-essentials: A package group that includes essential tools and utilities for building software in a Linux environment, such as compilers and build tools.
# default-libmysqlclient-dev: A package that includes development files needed for building applications that use the MySQL client library.
# note : installing unnecessary packages in your Docker image can expose your application to more vulnerabilities.

WORKDIR /app

COPY ./requirements.txt /app

RUN  pip install --no-cache-dir --requirement /app/requirements.txt

COPY ./app.py /app/

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]