FROM python:slim
WORKDIR /usr/app/src
COPY . ./
RUN pip install --default-timeout=100 -r /usr/app/src/requirements.txt
ENTRYPOINT [ "python3", "./pi_cctv_camera.py" ]
CMD [ "http://localhost:8000", "10", "0"]
