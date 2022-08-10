
#conda install -c conda-forge face_recognition
import cv2
import face_recognition

#read image
img = cv2.imread("images/Lionel Messi.jpg")

#convert it into RGB format
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#encode the image:
img_encoding = face_recognition.face_encodings(rgb_img)[0] #load mutiple images
print(img_encoding)


###
img2 = cv2.imread("images/Elon Musk.jpg")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

result = face_recognition.compare_faces([img_encoding], img_encoding2)  
print(result) #[False]



cv2.imshow("Img", img)
cv2.waitKey(0)

