FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get clean
RUN apt-get install -y nodejs npm && apt-get clean
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN mkdir /code
WORKDIR /code
RUN npm install -g bower
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install django-bower
ADD . /code/
