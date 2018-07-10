FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python3", "./startBot.py" ]
