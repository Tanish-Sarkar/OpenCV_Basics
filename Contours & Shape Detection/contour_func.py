import cv2
import sys

absolute_path = "OpenCV_Basics\Contours & Shape Detection\triangle.jpg"
image = cv2.imread(absolute_path) 

# CRITICAL CHECK: Always verify if the image loaded successfully
if image is None:
    print("ERROR: Could not open or find the image.")
    print(f"The path used was: {absolute_path}")
    sys.exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Finding Contour
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Drawing the Contour
cv2.drawContours(image, contours, -1, (0,255,0), 2)

for contour in contours:
    

cv2.imshow("Contoured image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()