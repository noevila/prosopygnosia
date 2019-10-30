import cv2
import os
import numpy as np
from PIL import Image

cascade = cv2.CascadeClassifier('./../../haarcascades/haarcascade_frontalface_alt.xml')


def cam_recognition():
    cam = cv2.VideoCapture(0)
    cv2.startWindowThread()
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
    exit()


def cam_recognition_with_ai(usernames_ids):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trained.yml')
    cam = cv2.VideoCapture(0)
    while True:
        exists, img = cam.read()
        if exists:
            greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(greyscale, 1.3, 5)
            for (x, y, w, h) in faces:
                rectangle = cv2.rectangle(img, (x, y), (x + w, y + h), (125, 255, 0), 2)
                user_id, conf = recognizer.predict(greyscale[y:y + h, x:x + w])
                if conf < 50:
                    name = usernames_ids[user_id]
                else:
                    name = "unknown"
                cv2.putText(rectangle, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2 )
            cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
    exit()


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


def train_ai(path):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    prof_path = [os.path.join(path, user) for user in os.listdir(path)]
    faces = []
    ids = []
    usernames_ids = {}
    for user in prof_path:
        if not os.path.isdir(user):
            continue
        user_path = [os.path.join(user, image) for image in os.listdir(user)]
        internal_id = np.random.randint(0, 100000)
        usernames_ids[internal_id] = ('@' + user[12:])
        for image in user_path:
            img = cv2.imread(image)
            greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img_np = np.array(greyscale, 'uint8')
            faces.append(img_np)
            ids.append(internal_id)
    recognizer.train(faces, np.array(ids))
    recognizer.save('trained.yml')
    return usernames_ids
