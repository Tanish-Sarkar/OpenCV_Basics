import cv2

image = cv2.imread("sample_images/00415-200124725.png")

if image is not None:
    print("Loaded")
    choice = input("Enter you choice(line, rectangle, circle, text): ")
    if (choice == "line"):
        print("Drawing Line on Image")
        
        print("For point 1")
        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))
        pt1 = (x1,y1)
        
        print("For point 2")
        x2 = int(input("Enter x2: "))
        y2 = int(input("Enter y2: "))
        pt2 = (x2,y2)

        print("For Color in rgb format: ")
        r = int(input("Enter r: "))
        g = int(input("Enter g: "))
        b = int(input("Enter b: "))
        color = (r,g,b)
        
        thickness = int(input("Enter the thickness of line: "))
        cv2.line(image, pt1, pt2, color, thickness)

    elif(choice == "rectangle"):
        print("Drawing Rectangle on Image")

        print("For point 1")
        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))
        pt1 = (x1,y1)
        
        print("For point 2")
        x2 = int(input("Enter x2: "))
        y2 = int(input("Enter y2: "))
        pt2 = (x2,y2)

        print("For Color in rgb format: ")
        r = int(input("Enter r: "))
        g = int(input("Enter g: "))
        b = int(input("Enter b: "))
        color = (r,g,b)
        
        thickness = int(input("Enter the thickness of border: "))
        cv2.rectangle(image, pt1, pt2, color, thickness)

    elif(choice == "circle"):
        print("Drawing Circle on Image")

        print("For center")
        x = int(input("Enter x1: "))
        y = int(input("Enter y1: "))
        center = (x,y)
        
        print("For radius")
        radius = int(input("Enter the radius: "))

        print("For Color in rgb format: ")
        r = int(input("Enter r: "))
        g = int(input("Enter g: "))
        b = int(input("Enter b: "))
        color = (r,g,b)
        
        thickness = int(input("Enter the thickness of border: "))
        cv2.circle(image, center, radius, color, thickness)

    elif(choice == "text"):
        print("Add Text on Image")

        text = input("Enter the text: ")

        print("For font start point")
        x = int(input("Enter x1: "))
        y = int(input("Enter y1: "))
        font_start = (x,y)

        font = cv2.FONT_HERSHEY_COMPLEX

        font_scale = float(input("Enter the size of text"))

        print("For Color in rgb format: ")
        r = int(input("Enter r: "))
        g = int(input("Enter g: "))
        b = int(input("Enter b: "))
        color = (r,g,b)
        
        thickness = int(input("Enter the thickness of line: "))
        cv2.putText(image, text, font_start, font, font_scale, color, thickness)
    else:
        print("Invalid choice!!")

    cv2.imshow(f"{choice}", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed...!!")