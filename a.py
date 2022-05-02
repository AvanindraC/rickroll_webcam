import pyvirtualcam
import cv2 as cv
with pyvirtualcam.Camera(width=640, height=480, fps=20) as cam:
    print(f'Using virtual camera: {cam.device}')
    b = cv.VideoCapture("rr.mp4")
    while True:
        isTrue, frame = b.read()
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        frame = cv.resize(frame, (640, 480))
        cam.send(frame)
        cam.sleep_until_next_frame()