FROM python:3.9


COPY web/requirements.txt /app/requirements.txt
RUN pip install -r app/requirements.txt
EXPOSE 8000
COPY . /app
WORKDIR /app


