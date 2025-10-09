import cv2

image = cv2.imread("sample_images/00414-200124724.png")

if image is not None:
    print("Loaded")
    resized = cv2.resize(image, (320,320))
    cv2.imshow(f"Original Image: {image}")
    cv2.imshow(f"Resized Image: {resized}")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed!!")
