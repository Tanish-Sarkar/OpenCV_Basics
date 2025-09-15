import cv2

# Loading the Image
image = cv2.imread("./sample_images/00413-200124723.png")

if image is None:
    print("Error: image is empty")
else:
    print("Image Retrived Successfully")

# Showing the image
if image is not None:
    cv2.imshow("Cat Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: image is empty")
