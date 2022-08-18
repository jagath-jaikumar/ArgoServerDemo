FROM python:3.9

WORKDIR /app

RUN apt-get update

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY model.onnx .
COPY classes.json .

CMD python -u main.py
