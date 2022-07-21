import cv2

# Team members : Yash Kumar Jain, Nataly Michail, Thi Truc linh le, Mohamad Serhan


#Face detection using image
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('test.jpg')  # Read the input image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert into grayscale
faces = face_cascade.detectMultiScale(gray, 1.1, 4)  # Detect faces
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow('Face Detection', img)
cv2.waitKey()

# Face detection using Live video
"""
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
#img = cv2.imread('test.png')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)

    # Display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()"""
