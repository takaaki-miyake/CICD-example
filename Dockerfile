FROM python:alpine

WORKDIR /app

COPY ./app /app

RUN pip install Flask

CMD ["python", "flask_test.py"]
