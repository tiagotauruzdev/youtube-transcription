FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY transcriber.py .
COPY n8n_workflow.json .

CMD ["python", "transcriber.py"]
