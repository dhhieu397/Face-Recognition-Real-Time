import cv2
import face_recognition
from simple_facerec import SimpleFacerec 


#Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")
# Load Camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    #Detect Faces:
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        # print(face_loc) 
        # top, left, bottom, right = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3] #top - right- bottom -left.
        
        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 280), 2) #size_text: 1 ; 
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4) #left-top, right-bottom #green: (0, 0, 200); thick=4



    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27: #key from key board
        break


        ###color: black (0, 0, 0); red (0, 0, 280)