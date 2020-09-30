FROM python:3.7

COPY . /app

RUN pip install fastapi uvicorn

RUN pip install -r requirements.txt

EXPOSE 80


CMD ["uvicorn", "fastapp:app", "--host", "0.0.0.0", "--port", "80"]