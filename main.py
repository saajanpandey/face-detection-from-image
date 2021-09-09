#Simple face detection in image

import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read the input
img = cv2.imread('images/photo.jpeg')

# Detect faces
faces = face_cascade.detectMultiScale(img, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
   cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

#Export the Result
cv2.imwrite("face_detected.png", img)

print('Successfully saved')
