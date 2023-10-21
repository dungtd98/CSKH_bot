FROM python:3.10
ENV PYTHONWRITEBYCODE 1
ENV PYTHONUBUFFERED 1

EXPOSE 8000

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN mkdir -p /app/assets \
    && mkdir -p /app/logs \
    && chmod 755 /app \
    && pip install --no-cache-dir -r /app/requirements.txt

COPY . /app 

CMD ["/src/docker-entrypoint.sh", "-n"]