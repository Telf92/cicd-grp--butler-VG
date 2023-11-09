FROM python:3.9-slim

WORKDIR /backend

COPY backend/ .

RUN pip install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
