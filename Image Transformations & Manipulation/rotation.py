import cv2

image = cv2.imread("sample_images/00421-200124731.png")

if image is not None:
    print("Loaded")

    (h,w) = image.shape[:2]
    center = (w//2, h//2)
    # M = cv2.getRotationMatrix2D(center, angle, scale)
    M = cv2.getRotationMatrix2D(center, 60, 1.0)
    rotated = cv2.warpAffine(image, M, (w,h))

    cv2.imshow("original", image)
    cv2.imshow("Rotated", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Failed..!!")