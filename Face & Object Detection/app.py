import cv2

face_cascade = cv2.CascadeClassifier("OpenCV_Basics\Face & Object Detection\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    """
    detectMultiScale([image], [scale], [min no. of neightbour]) -> dectect face
    """