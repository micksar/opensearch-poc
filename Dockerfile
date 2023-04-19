FROM python:3.8

WORKDIR /app

COPY app/ .
# Install Elasticsearch-Py library (pinned to version 7.0.5)
RUN pip3 install elasticsearch==7.0.5

CMD ["python3", "main.py"]