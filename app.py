from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return "Smart Log Analyzer Running Successfully!"

@app.route('/health')
def health():
    return {
        "status": "running",
        "project": "Smart Log Analyzer"
    }

@app.route('/upload', methods=['POST'])
def upload_file():

    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    return jsonify({
        "message": "File uploaded successfully",
        "filename": file.filename
    })


@app.route('/analyze/<filename>')
def analyze_logs(filename):

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404

    error_count = 0
    warning_count = 0
    info_count = 0

    with open(filepath, 'r') as file:
        logs = file.readlines()

        for line in logs:

            if 'ERROR' in line:
                error_count += 1

            elif 'WARNING' in line:
                warning_count += 1

            elif 'INFO' in line:
                info_count += 1

    return jsonify({
        "ERROR": error_count,
        "WARNING": warning_count,
        "INFO": info_count
    })    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)