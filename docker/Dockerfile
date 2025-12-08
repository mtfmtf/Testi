FROM python:3.11-slim
WORKDIR /app/cfp
RUN apt-get update && apt-get install -y --no-install-recommends \
  nano \
  && rm -rf /var/lib/apt/lists/*
COPY ../python/test.py /app/test.py
RUN chmod +x /app/test.py
CMD ["python3.11", "test.py"]
