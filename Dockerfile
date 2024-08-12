FROM python:3.11-slim

RUN mkdir -p /home/dataeng
WORKDIR /home/dataeng

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m unittest discover -s tests

CMD ["python", "src/main.py"]
