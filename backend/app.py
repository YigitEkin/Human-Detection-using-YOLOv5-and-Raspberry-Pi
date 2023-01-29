import base64

import cv2  # type: ignore
import numpy as np
import torch
import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Image(BaseModel):
    data: str
    timestamp: str


image: Image = Image(data="", timestamp="")


def generate_bounding_box_with_yolo(data: str):
    nparr = np.frombuffer(base64.b64decode(data), np.uint8)
    one_d_arr = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    predict_image = model(one_d_arr)
    predict_image.render()
    yolo_bb_img = predict_image.ims[0]
    im_base64 = np.array(yolo_bb_img)
    _, jpg_converted_ig = cv2.imencode(".jpg", im_base64)
    yolo_byte_buffer = jpg_converted_ig.tobytes()
    base64_encoded_img: bytes = base64.b64encode(yolo_byte_buffer)
    return base64_encoded_img.decode("utf-8")


@app.post("/")
def append_image(data: Image) -> dict:
    global image
    image = Image(data=generate_bounding_box_with_yolo(data.data),
                    timestamp=data.timestamp)
    return {"data": "image successfully appended"}


@app.get("/")
def get_latest_image(request: Request):
    global image
    if image.data != "":
        return templates.TemplateResponse("index.html",
                                          {"request": request,
                                           "data": image.data,
                                           "timestamp": image.timestamp})
    return templates.TemplateResponse("empty.html", {"request": request})


if __name__ == "__main__":
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', force_reload=True)
    PERSON_CLASS_LABEL = 0
    model.classes = [PERSON_CLASS_LABEL]
    model.conf = 0.45
    uvicorn.run(app, host="0.0.0.0", port=8000)
