FROM python:3.12-slim-bullseye

ENV PYTHONUNBUFFERED True
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py", "--host", "0.0.0.0", "--port", "8080"]