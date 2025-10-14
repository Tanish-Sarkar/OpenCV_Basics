import cv2

image = cv2.imread("sample_images/00419-200124729.png")

# cv2.medianBlur(image, kernel_size)
medium_blur = cv2.medianBlur(image, 5)

cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", medium_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()