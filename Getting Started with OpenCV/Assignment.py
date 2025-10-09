import cv2

# 1. load image 
image = cv2.imread("sample_images/00415-200124725.png")

if image is not None:
    # 2. grayscaling
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    choice = int(input("What you want \n(1)Show the image \n(2)Save the image\n"))
    if choice == 1:
        showing_name = input("Enter the Showing name of th Image: ")
        # 3. showing grayscaled image
        cv2.imshow(f"{showing_name}", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choice == 2:
        saving_name = input("Enter the Saving name of th Image: ")
        # 4. saving the Image
        success = cv2.imwrite(f'sample_images\{saving_name}.png', gray)
        print("Saved Successfully!!!")
    else:
        print("Operation error occurred....")
else:
    print("Load the image Properly")
