from flask import Flask, jsonify
import requests
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Prometheus metric
REQUEST_COUNT = Counter('frontend_requests_total', 'Total requests to frontend')

@app.route("/call-backend")
def call_backend():
    REQUEST_COUNT.inc()
    try:
        response = requests.get("http://backend-service:5000/data")
        return jsonify({"frontend": "Hello from Frontend!", "backend": response.json()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/metrics")
def metrics():
    return generate_latest(REQUEST_COUNT)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
