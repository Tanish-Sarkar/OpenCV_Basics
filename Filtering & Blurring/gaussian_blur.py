import cv2

image = cv2.imread("sample_images/00420-200124730.png")

# cv2.GaussianBlur(image, (kernal_start, kernel_end), sigma)
gaussian_blur = cv2.GaussianBlur(image, (7,7), 0)

cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", gaussian_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()