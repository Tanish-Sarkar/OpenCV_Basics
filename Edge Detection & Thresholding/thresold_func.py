import cv2

image = cv2.imread("OpenCV_Basics\sample_images\CAT_IMG.png", cv2.IMREAD_GRAYSCALE)

ret, thres_img = cv2.threshold(image, 120, 155, cv2.THRESH_BINARY)

cv2.imshow("Original images", image)
cv2.imshow("Edges", thres_img)
cv2.waitKey(0)
cv2.destroyAllWindows() 