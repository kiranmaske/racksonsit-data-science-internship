import cv2

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("D:/Internship_June2025/project/mini/haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("D:/Internship_June2025/project/mini/haarcascade_smile.xml")

cnt = 500  # Move counter outside loop to avoid resetting every frame

while True:
    success, img = video.read()
    if not success:
        break

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayImg, 1.1, 4)
    keyPressed = cv2.waitKey(1)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 3)
        roi_gray = grayImg[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 15)

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(img, (x + sx, y + sy), (x + sx + sw, y + sy + sh), (100, 100, 100), 5)
            print("Image " + str(cnt) + " Saved")
            path = f'./img{cnt}.jpg'  # Fixed file extension and used f-string
            cv2.imwrite(path, img)
            cnt += 1
            if cnt >= 503:
                break

    cv2.imshow("live video", img)
    if keyPressed & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()