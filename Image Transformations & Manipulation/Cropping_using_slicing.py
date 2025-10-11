import cv2

image = cv2.imread("sample_images/00421-200124731.png")

if image is not None:
    print("Loaded")
    cropped = image[100:200, 15:150]  # image[startY:endY, startX: endX]
    cv2.imshow("Cropped", cropped)
    cv2.imshow("original", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Failed..!!")