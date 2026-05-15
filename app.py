from flask import Flask, request, jsonify
import re
from collections import Counter

app = Flask(__name__)

ERROR_PATTERNS = [
    r'error',
    r'failed',
    r'timeout',
    r'unauthorized',
    r'critical'
]

def analyze_logs(logs):
    results = []
    counts = Counter()

    for line in logs.splitlines():
        status = "Normal"

        for pattern in ERROR_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                status = "Anomaly"
                counts[pattern] += 1

        results.append({
            "log": line,
            "status": status
        })

    return results, counts

@app.route('/')
def home():
    return "Smart Log Analyzer Running"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    logs = data.get("logs", "")

    analyzed_logs, counts = analyze_logs(logs)

    return jsonify({
        "results": analyzed_logs,
        "summary": counts
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)