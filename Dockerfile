FROM python:3.7
MAINTAINER mirismr
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD exec python3 manage.py makemigrations
CMD exec python3 manage.py migrate
CMD exec python3 manage.py runserver