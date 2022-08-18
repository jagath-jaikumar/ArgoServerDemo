FROM python:3.9

WORKDIR /app

RUN apt-get update

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6999", "--workers", "1", "--timeout-keep-alive", "120", "--log-level", "info"]
