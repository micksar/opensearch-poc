FROM python:3.9

WORKDIR /app

COPY app/ .
# Install Elasticsearch-Py library (pinned to version 7.0.5)
RUN pip3 install opensearch-py

EXPOSE 9200

CMD ["python3", "main.py"]