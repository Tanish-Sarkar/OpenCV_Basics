import cv2

# 1. load image 
image = cv2.imread("sample_images/00415-200124725.png")

if image is not None:
    # 2. grayscaling
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 3. showing grayscaled image
    cv2.imshow("Gray scaled Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # 4. saving the Image
    success = cv2.imwrite('sample_images\ASS.png', gray)
    print("Saved Successfully!!!")
else:
    print("Load the image Properly")