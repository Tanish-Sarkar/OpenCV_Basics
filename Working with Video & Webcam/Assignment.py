import cv2

camera = cv2.VideoCapture(0)

choice = input("Do you want to save the video recording (YES/NO): ").upper()

# Initialize recorded variable to None
recorded = None

if (choice == "YES"):
    print("Video will be saved after recording!")
    
    # FIX 2: Corrected property from WEIGHT to WIDTH
    frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    codec = cv2.VideoWriter_fourcc(*'XVID')
    recorded = cv2.VideoWriter("Project_video.mp4", codec, 20.0, (frame_width, frame_height))

else:
    print("Video will not be saved after recording.")

while True:
    success, image = camera.read()
    if not success:
        print("Failed to capture frame.")
        break
    
    # FIX 1: Only write to the file if the VideoWriter object was created
    if choice == "YES":
        recorded.write(image)

    cv2.imshow("Recording Live", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

# Release resources properly
camera.release()

# Also release the writer object if it was created
if recorded is not None:
    recorded.release()
    
cv2.destroyAllWindows()