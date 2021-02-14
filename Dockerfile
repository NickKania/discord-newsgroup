FROM python:3.8.5

COPY requirements.txt /tmp/requirements.txt
WORKDIR /tmp

RUN pip install -r requirements.txt

WORKDIR dev/
COPY src/ .

CMD ["python", "./bot.py"]
