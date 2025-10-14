import cv2
import numpy as np

image = cv2.imread("sample_images/00422-200124732.png")

sharpen_kernal = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

# cv2.filter2D(image, depth, sharpen_kernal)
sharped = cv2.filter2D(image, -1, sharpen_kernal)

cv2.imshow("Original Image", image)
cv2.imshow("Shappened Image", sharped)

cv2.waitKey(0)
cv2.destroyAllWindows()