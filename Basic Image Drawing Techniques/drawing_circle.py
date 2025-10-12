import cv2

image = cv2.imread("sample_images/00415-200124725.png")

if image is not None:
    print("Loaded")

    center = (150,150)
    radius = 50
    color = (0,255,0)
    thickness = 2  # -ve value to fill the cirle and +ve value for borders only
    cv2.circle(image, center, radius, color, thickness)

    cv2.imshow("cirle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Failed...!!")

