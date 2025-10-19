import cv2

image = cv2.imread("OpenCV_Basics\sample_images\CAT_IMG.png", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(image, 50, 150 ) # (image, thresold1, thresold2)

cv2.imshow("Original images", image)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows() 