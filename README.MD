# Human Detection using YOLOv5 and Raspberry Pi

A project that detects humans in real-time using a Raspberry Pi camera and YOLOv5 object detection model. The project consists of two parts: camera module and backend server.

## Getting Started

These instructions will guide you through the process of setting up and running the project.

## Installation

- Clone the repository
- Navigate to the camera_module directory and follow the instructions in the README file to run the camera module
- Navigate to the backend directory and follow the instructions in the README file to run the backend server.

## Usage

The camera module takes photos at a specified interval and sends the images to the backend server. The backend server processes the images using YOLOv5 to detect humans and sends the result back to the client as a base64 encoded HTML file with server-side rendering. The HTML file includes the timestamp and the processed image.

## Acknowledgments

- YOLOv5 object detection model by [Ultralytics LLC](https://github.com/ultralytics/yolov5)
- [Raspberry Pi Foundation](https://www.raspberrypi.org/)
