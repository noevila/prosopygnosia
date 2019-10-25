import cv2
import os

cascade = cv2.CascadeClassifier('./../../haarcascades/haarcascade_frontalface_alt.xml')


def cam_recognition():
    cam = cv2.VideoCapture(0)
    while True:
        exists, img = cam.read()
        if exists:
            greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(greyscale, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (125, 255, 0), 2)
            cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()


def count_faces(image_path):
    img = cv2.imread(image_path)
    greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(greyscale, 1.3, 5)
    return len(faces)


def number_of_faces(image_path):
    if not count_faces(image_path) == 1:
        os.remove(image_path)
        return 1
    else:
        return 0


def crop_face(image_path):
    img = cv2.imread(image_path)
    greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = cascade.detectMultiScale(greyscale, 1.3, 5)
    (x, y, w, h) = face[0]
    crop_img = img[y:y+h, x:x+w]
    os.remove(image_path)
    cv2.imwrite(image_path, crop_img)
    return
