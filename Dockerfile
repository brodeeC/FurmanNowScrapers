FROM python:3.11-slim
WORKDIR /app

COPY ./ .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY create_db.sh .
RUN chmod +x create_db.sh && \
    if ! ./create_db.sh; then \
        echo "Script failed!" >&2; \
        exit 1; \
    fi

COPY updateAll.sh .
RUN chmod +x updateAll.sh 

EXPOSE 8080
CMD ["gunicorn", "backend.main:app", "-b", "0.0.0.0:8080"]