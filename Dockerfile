# pull official base image
FROM python:3.8.3-alpine
# set work directory
WORKDIR /usr/src/backend
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY ./vova_app/requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY ./vova_app /usr/src/backend