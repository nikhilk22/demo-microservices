FROM python:3.12-slim
WORKDIR /app
COPY frontend.py .
RUN pip install --break-system-packages flask requests prometheus_client
CMD ["python", "frontend.py"]
