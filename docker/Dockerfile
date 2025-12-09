FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
  nano \
  && rm -rf /var/lib/apt/lists/*
COPY ../python /app/
RUN chmod +x /app/workflow.sh
RUN mkdir docs
RUN mkdir user
COPY ../user /app/user/
ENTRYPOINT ["./workflow.sh"]
CMD ["bash"]
