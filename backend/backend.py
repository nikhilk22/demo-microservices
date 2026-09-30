from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Prometheus metric
REQUEST_COUNT = Counter('backend_requests_total', 'Total requests to backend')

@app.route("/data")
def get_data():
    REQUEST_COUNT.inc()
    return jsonify({"message": "Hello from Backend!"})

@app.route("/metrics")
def metrics():
    return generate_latest(REQUEST_COUNT)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
