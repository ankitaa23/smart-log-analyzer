# Smart Log Analyzer

A cloud-based smart log analyzer built using Flask, Docker, GitHub Actions CI/CD, and AWS.


## Features

- Log file upload
- Error and warning detection
- REST APIs
- Docker containerization
- GitHub Actions CI/CD
- AWS EC2 deployment


## Tech Stack

- Python
- Flask
- Docker
- GitHub Actions
- AWS EC2
- Gunicorn
- Postman


## Project Structure

smart-log-analyzer/
│
├── .github/
├── uploads/
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore



## Run Locally

```bash
pip install -r requirements.txt
python app.py
```


## Docker Run

```bash
docker build -t smart-log-analyzer .
docker run -p 5000:5000 smart-log-analyzer
```


## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | / | Home Route |
| GET | /health | Health Check |
| POST | /upload | Upload Log File |
| GET | /analyze/<filename> | Analyze Uploaded Logs |


## Future Improvements

- ML anomaly detection
- Dashboard visualization
- Real-time monitoring
- Kubernetes deployment
- Alert notification system