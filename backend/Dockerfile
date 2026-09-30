FROM python:3.12-slim
WORKDIR /app
COPY backend.py .
RUN pip install --break-system-packages flask prometheus_client
CMD ["python", "backend.py"]
