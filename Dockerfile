FROM python:3-slim-buster
COPY requirements.txt /
RUN pip install -r requirements.txt
WORKDIR /app
COPY src/ /app
CMD ["python3","main.py"]
