FROM python:3.7-slim

ADD /static /flask/static
ADD requirements.txt /flask
ADD app.py /flask
WORKDIR /flask

RUN apt-get update && \
  apt-get install -y graphviz && \
  pip install -r requirements.txt

ENTRYPOINT [ "python", "app.py" ]
EXPOSE 5000
