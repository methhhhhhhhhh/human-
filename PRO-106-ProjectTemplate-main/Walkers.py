import cv2


# Create our body classifier
bodyclassifier = cv2.CascadeClassifier('haarcascade_fullybody.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()

    #Convert Each Frame into Grayscale
    cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pass frame to our body classifier
    bodies = body_classifiier.dectect =MultiScale(gray, 1.2, 3)
    
    # Extract bounding boxes for any bodies identified
    cv2.imshow()

    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
