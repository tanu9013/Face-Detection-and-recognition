import cv2
harcascade= "haarcascade_frontalface_default.xml"
cap = cv2.VideoCapture(1)

cap.set(3,640)
cap.set(4, 480)
while True:
    success, img = cap.read()

    facecascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("face", img_gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
