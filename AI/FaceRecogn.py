import cv2
import face_recognition

img = cv2.imread("Arhaan.webp")
rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# img_encoding = face_recognition.face_encodings(rgb_img)[0]

cv2.imshow("Img",img)
cv2.waitKey(1)

