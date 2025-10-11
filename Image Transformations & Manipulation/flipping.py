import cv2

image = cv2.imread("sample_images/00421-200124731.png")

if image is not None:
    print("Loaded")

    flipped_horizontal = cv2.flip(image,1)
    flipped_vertical = cv2.flip(image,0)
    flipped_both = cv2.flip(image,-1)

    cv2.imshow("flipped Horiontal", flipped_horizontal)
    cv2.imshow("flipped Vertical", flipped_vertical)
    cv2.imshow("flipped both", flipped_both)

    cv2.imshow("original", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Failed..!!")