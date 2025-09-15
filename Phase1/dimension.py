import cv2

image = cv2.imread("sample_images\CAT_IMG.png")

if image is not None:
    h,w,c = image.shape
    print(f"Image Dimensions are: Height: {h}, Width: {w}, Channels: {c}")
else:
    print("Load the Image Properly")
