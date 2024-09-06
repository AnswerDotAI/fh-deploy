FROM python:3.10

WORKDIR /code
COPY --link --chown=1000 . .

RUN mkdir -p /tmp/cache/
RUN chmod a+rwx -R /tmp/cache/
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1 PORT=5001

CMD ["python", "main.py"]
