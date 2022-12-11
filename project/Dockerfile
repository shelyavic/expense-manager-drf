# pull official base image
FROM python:3.10-slim-bullseye

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 1
ENV SECRET_KEY "&7uy^(!$#-(f3etye&ll5xcy3(k16*+xgu0l=o0p-oj_vhs($4"
ENV DJANGO_ALLOWED_HOSTS "localhost 127.0.0.1 [::1]"

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]