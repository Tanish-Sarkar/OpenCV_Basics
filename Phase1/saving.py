import cv2

image = cv2.imread("./sample_images/00413-200124723.png")

if image is not None:
    cv2.imshow("Cat Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # -------- Saving the Image -------------
    cv2.imwrite("./sample_images/CAT_IMG.png", image)

else:
    print("Load the Image Correctly")