FROM python:3.11-alpine

COPY app /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9374

COPY --chown=root entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]