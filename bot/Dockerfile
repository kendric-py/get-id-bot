FROM python:3.10.10

WORKDIR /bot

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD python -u src