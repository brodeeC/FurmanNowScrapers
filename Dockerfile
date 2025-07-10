FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY updateAll.sh .
RUN chmod +x updateAll.sh

COPY ./ . 

EXPOSE 8080
CMD ["gunicorn", "backend.main:app", "-b", "0.0.0.0:8080"]