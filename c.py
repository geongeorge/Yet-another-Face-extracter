import cv2
from utils.tools import flip
import os

# Load the cascade
face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')

#It seems this only detects faces turned right
right_face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_profileface.xml')
# Fix by applying 2 turns , one with image flipped

#get image name from arguements later (using arguement-parser)
imageName = "test2.jpg"

# Read the input image
img = cv2.imread(imageName)

#flip horizontal
# img = flip(img,1)

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces using cascades
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

#make o/p folder id does not exist
os.makedirs("output", exist_ok=True)

# Draw rectangle around the faces
count=0
for (x, y, w, h) in faces:
    # Mark rectangles to show
    # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    #clever hack :P
    #Here do something to disregard smaller sizes (idunno maybe 70px min width or height)
    minWidth = minHeight = 70
    if(w<=minWidth or h<=minHeight):
        continue
        #ignore
    #else save
    #cropped image
    crop_img = img[y:y+h, x:x+w]
    cv2.imwrite("output/"+str(count)+".jpg", crop_img)
    count+=1


    
    
# Display the output
cv2.imshow('img', img)
cv2.waitKey(0)