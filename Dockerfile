FROM python:3.9-slim

WORKDIR /backend

COPY backend/ .

RUN pip install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["curl", "-dp", "5000:5000", "curlcontainer", "flask", "run"]
