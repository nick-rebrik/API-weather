FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . .

RUN mkdir -p ./logs && chmod 777 ./logs

RUN chmod 777 ./entrypoint.sh