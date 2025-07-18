FROM python:3.11-slim
WORKDIR /app

RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

COPY ./ .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY create_db.sh .
RUN chmod +x create_db.sh

COPY updateAll.sh .
RUN chmod +x updateAll.sh

COPY updateRoute.sh .
RUN chmod +x updateRoute.sh

RUN touch /var/log/cron.log


# RUN echo "0 */4 * * * root /bin/sh /app/updateRoute.sh >> /var/log/cron.log 2>&1" > /etc/cron.d/updatejob \
#     && chmod 0644 /etc/cron.d/updatejob
RUN echo "*/2 * * * * root /bin/sh /app/updateRoute.sh >> /var/log/cron.log 2>&1" > /etc/cron.d/updatejob && chmod 0644 /etc/cron.d/updatejob

RUN service cron start

EXPOSE 8080