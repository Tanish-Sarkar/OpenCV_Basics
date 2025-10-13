import cv2

camera = cv2.VideoCapture(0)

choice = input("do you want to save the video recording (YES/NO): ")

if (choice == "YES"):
    print("Vedio will be saved after recording!")
    frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WEIGHT))
    frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    codec = cv2.VideoWriter_fourcc(*'XVID')

    recorded = cv2.VideoWriter("Project_video.mp4", codec, 20, (frame_width, frame_height))

else:
    print("Video will not be saved after recording")

while True:
    success, image = camera.read()
    if not success:
        break

    recorded.write(image)
    cv2.imshow("Recording Live", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

camera.release()
cv2.destroyAllWindows()