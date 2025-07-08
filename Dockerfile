FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

EXPOSE 8080

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:8080"]

RUN apt-get update && apt-get install -y cron

COPY updateAll.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/updateAll.sh

RUN echo "0 * * * * /usr/local/bin/updateAll.sh" | crontab -