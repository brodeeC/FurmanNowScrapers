FROM python:3.11-slim
WORKDIR /app

ENV SUPERCRONIC_URL=https://github.com/aptible/supercronic/releases/download/v0.2.29/supercronic-linux-amd64 \
    SUPERCRONIC=supercronic-linux-amd64 \
    SUPERCRONIC_SHA1SUM=cd48d45c4b10f3f0bfdd3a57d054cd05ac96812b
RUN curl -fsSLO "$SUPERCRONIC_URL" \
    && echo "${SUPERCRONIC_SHA1SUM} ${SUPERCRONIC}" | sha1sum -c - \
    && chmod +x "$SUPERCRONIC" \
    && mv "$SUPERCRONIC" "/usr/local/bin/${SUPERCRONIC}" \
    && ln -s "/usr/local/bin/${SUPERCRONIC}" /usr/local/bin/supercronic

COPY ./ .

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x create_db.sh

RUN chmod +x updateAll.sh

RUN touch /var/log/cron.log

COPY crontab /app/crontab
RUN chmod 0644 /app/crontab

EXPOSE 8080