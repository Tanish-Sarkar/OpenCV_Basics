import cv2

image = cv2.imread("sample_images/00415-200124725.png")

if image is not None:
    print("Loaded")

    text = "This is Zac"
    font_start = (50,300)  # the bottom-left point of text
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1.2
    color = (0,255,0)
    thickness = 2  
    cv2.putText(image, text, font_start,font, font_scale, color, thickness)

    cv2.imshow("Adding text to image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Failed...!!")

