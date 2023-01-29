FROM python:3.8
WORKDIR /usr/app/src
COPY . ./
RUN pip3 install --default-timeout=100 -r requirements.txt
ENTRYPOINT [ "python3", "./app.py" ]
