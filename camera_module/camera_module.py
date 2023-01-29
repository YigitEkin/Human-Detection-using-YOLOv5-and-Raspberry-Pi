import argparse
import base64
import time
from argparse import ArgumentParser
# type: ignore
from datetime import datetime

from cv2 import VideoCapture  # type: ignore
from cv2 import imencode
from requests import post


def capture_timelapsed_images(url: str,
                              delay: int = 10,
                              port: int = 0) -> None:
    cam_port: int = port
    delay_between_captures: int = delay
    cam = VideoCapture(cam_port)
    while True:
        result, image = cam.read()
        if result:
            _, im_arr = imencode('.jpg', image)
            im_bytes = im_arr.tobytes()
            im_b64: bytes = base64.b64encode(im_bytes)
            decoded_base64_str: str = im_b64.decode("utf-8")
            json_to_send = {
                "data": decoded_base64_str,
                "timestamp": str(datetime.now())
            }
            post(url, json=json_to_send)
        time.sleep(delay_between_captures)


def arg_parser() -> argparse.Namespace:
    parser: ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("url", type=str, nargs="?",
                        help="url for sending the streamed images",
                        default="http://localhost:8000")
    parser.add_argument("delay", type=int, nargs="?",
                        help="time difference between images in seconds.",
                        default=10)
    parser.add_argument("port", type=int, nargs="?",
                        help="camera port to be used.", default=0)
    opt: argparse.Namespace = parser.parse_args()
    return opt


def main() -> None:
    args: argparse.Namespace = arg_parser()
    delay: int = args.delay
    port: int = args.port
    url: str = args.url
    capture_timelapsed_images(delay=delay, port=port, url=url)


if __name__ == "__main__":
    main()
