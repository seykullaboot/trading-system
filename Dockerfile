FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \n    gcc \n    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p logs

ENV PYTHONUNBUFFERED=1
ENV LOG_LEVEL=INFO

EXPOSE 5001 5002 5003 5004

CMD ["python", "main.py"]