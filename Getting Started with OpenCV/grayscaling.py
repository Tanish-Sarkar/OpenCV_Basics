import cv2

image = cv2.imread("sample_images\CAT_IMG.png")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    success = cv2.imwrite("sample_images/CAT_BnW.png", gray)
    print("The Image is successfully converted and printed")
else:
    print("Load the Image Properly")
