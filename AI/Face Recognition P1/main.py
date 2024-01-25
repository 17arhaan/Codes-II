import cv2
import face_recognition
from face_recgn import Facerecogn 

camr = cv2.VideoCapture(1)
while True:
    ret , frame = camr.read()
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

camr.release()
cv2.destroyAllWindows


# img = cv2.imread("Arhaan.webp")
# rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img_encoding = face_recognition.face_encodings(rgb_img)


# cv2.imshow("Image",img)
# cv2.waitKey(1)

