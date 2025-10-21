# OpenCV Mastery Journey — From Pixels to Perception 👁️‍🗨️

Welcome to my OpenCV learning repository!  
This project documents my complete hands-on journey through the fascinating world of **Computer Vision**, exploring how machines *see*, *process*, and *understand* images and videos.

---

##  Course Overview

> This course took me from the basics of reading an image to real-time **face and object detection** using Haar Cascades — all with Python and OpenCV.
The entire course was divided into **8 phases**, each focusing on a core aspect of computer vision:

---

## 🧩 Learning Path

```mermaid
graph TD;
A[Phase 0: Getting Ready] --> B[Phase 1: Getting Started];
B --> C[Phase 2: Image Transformations];
C --> D[Phase 3: Drawing Techniques];
D --> E[Phase 4: Video & Webcam];
E --> F[Phase 5: Image Filtering];
F --> G[Phase 6: Edge Detection];
G --> H[Phase 7: Contours & Shape Detection];
H --> I[Phase 8: Face & Object Detection];
````

---

## Phase Breakdown

| **Phase** | **Title**                            | **Key Learnings**                                                                                                                                                             |
| --------- | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **0**     | Getting Ready for OpenCV             | Introduction to OpenCV, Importance of Computer Vision, Use cases, Key features & prerequisites                                                                                |
| **1**     | Getting Started with OpenCV          | Installing `cv2`, Reading/displaying/saving images, Working with channels, Grayscale conversion                                                                               |
| **2**     | Image Transformations & Manipulation | Resizing, Cropping, Rotating, Flipping, Drawing shapes, Adding text and annotations                                                                                           |
| **3**     | Basic Image Drawing Techniques       | Drawing lines, rectangles, circles, and creating custom graphic overlays                                                                                                      |
| **4**     | Working with Video & Webcam          | Capturing live video (`cv2.VideoCapture()`), Frame-by-frame processing, Real-time filters, Saving video (`cv2.VideoWriter()`)                                                 |
| **5**     | Image Filtering & Blurring           | Gaussian blur, Median blur, Sharpening filters, Smoothing noisy images, Enhancing clarity                                                                                     |
| **6**     | Edge Detection & Thresholding        | Canny edge detection, Binary & adaptive thresholding, Bitwise operations (AND, OR, NOT), Extracting outlines                                                                  |
| **7**     | Contours & Shape Detection           | Finding and drawing contours, Shape detection using `approxPolyDP()`, Object recognition basics                                                                               |
| **8**     | Face & Object Detection              | Haar Cascade Classifiers, Face/eye/smile detection, Pre-trained models, Bounding boxes — [Haar Cascade Files](https://github.com/opencv/opencv/tree/master/data/haarcascades) |


---

## 🧠 Key Takeaways

* ✅ Learned how images are represented as arrays
* ✅ Applied image transformations and filters
* ✅ Built real-time video processing pipelines
* ✅ Implemented face & object detection systems
* ✅ Gained strong foundational understanding of Computer Vision

---

## Tech Stack

| Tool / Library                 | Purpose                     |
| ------------------------------ | --------------------------- |
| **Python**                     | Core programming language   |
| **OpenCV (cv2)**               | Image & video processing    |
| **NumPy**                      | Matrix & pixel manipulation |
| **Jupyter Notebook / VS Code** | Development environment     |

---

## Example Code Snippet

```python
import cv2

# Load image
img = cv2.imread('face.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load pre-trained classifier from OpenCV GitHub
# You can find the XML files here: https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 🧭 My Next Step

I’ll soon integrate OpenCV with **Deep Learning models** to make vision systems smarter and more adaptive — moving from *seeing* to *understanding.*

---

## 🪄 About Me

👋 Hi, I’m **Tanish Sarkar**, a Computer Engineering student passionate about AI, NLP ,Computer Vision, Data Science, system Design and full-stack development.
I love exploring how technology can make machines *see, think,* and *act* intelligently.

Let’s connect on [LinkedIn](https://www.linkedin.com/in/tanish-sarkar/) 🚀

---

## 🌟 Acknowledgements

Huge thanks to the amazing open-source community behind **OpenCV** for making such powerful computer vision tools accessible to everyone.

---

#OpenCV #ComputerVision #Python #MachineLearning #DeepLearning #AI #DataScience #ImageProcessing #TechJourney #LearningInPublic #Developers
