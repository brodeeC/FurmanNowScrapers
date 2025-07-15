FROM python:3.11-slim
WORKDIR /app

RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

COPY ./ .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY updateAll.sh .
RUN chmod +x updateAll.sh

RUN echo "0 */4 * * * root /bin/sh /app/updateAll.sh >> /var/log/cron.log 2>&1" > /etc/cron.d/updatejob \
    && chmod 0644 /etc/cron.d/updatejob

EXPOSE 8080