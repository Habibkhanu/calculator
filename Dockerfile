FROM python:3.10-slim
WORKDIR /app
COPY calculator.py .
COPY batch_calculator.py .
COPY batch_runner.py .
COPY data/ ./data/
ENTRYPOINT ["python", "batch_runner.py"]
