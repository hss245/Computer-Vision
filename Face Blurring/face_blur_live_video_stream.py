import numpy as np
import cv2
import dlib

video_capture = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

blurred = False
framed = False

while True:
    ret, frame = video_capture.read()
    if (ret):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)
        for rect in rects:
            x = rect.left()
            y = rect.top()
            x1 = rect.right()
            y1 = rect.bottom()
            if blurred:
                frame[y:y1, x:x1] = cv2.blur(frame[y:y1, x:x1], (25, 25))
            if framed:
                cv2.rectangle(frame, (x, y), (x1, y1), (0, 0, 255), 2)
        cv2.imshow('Video Feed', frame)
    ch = 0xFF & cv2.waitKey(1)
    if ch == ord("b"):
        blurred = not blurred
    if ch == ord("f"):
        framed = not framed
    if ch == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
