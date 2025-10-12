import cv2

image = cv2.imread("sample_images/00415-200124725.png")

if image is not None:
    print("Loaded")

    pt1 = (50,100) # top-left point
    pt2 = (300,300) # bottom-right point
    color = (0,255,0)
    thickness = 4

    cv2.rectangle(image, pt1, pt2, color, thickness)

    cv2.imshow("Line", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Failed...!!")