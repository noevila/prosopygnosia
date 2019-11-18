import cv2
import os
import numpy as np
from PIL import Image

cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')


def cam_recognition():
    # Initialization of the cv2 cam module in a new window
    cam = cv2.VideoCapture(0)
    cv2.startWindowThread()
    # Loop refreshing images
    while True:
        exists, img = cam.read()
        if exists:
            # For the comparative I need the image in grayscale.
            greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Detects the coordinates of the face
            # cascade.detectMultiScale(image, scaleFactor,minNeighbors)
            faces = cascade.detectMultiScale(greyscale, 1.3, 5)
            for (x, y, w, h) in faces:
                # Draw the rectangle around the face
                cv2.rectangle(img, (x, y), (x + w, y + h), (125, 255, 0), 2)
            cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
    exit()


def cam_recognition_with_ai(usernames_ids):
    # Initialization of the cv2 cam module in a new window
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trained.yml')
    cam = cv2.VideoCapture(0)
    # Loop refreshing images
    while True:
        exists, img = cam.read()
        if exists:
            # For the comparative I need the image in grayscale.
            greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Detects the coordinates of the face
            # cascade.detectMultiScale(image, scaleFactor,minNeighbors)
            faces = cascade.detectMultiScale(greyscale, 1.3, 5)
            for (x, y, w, h) in faces:
                # Draw the rectangle around the face
                rectangle = cv2.rectangle(img, (x, y), (x + w, y + h), (125, 255, 0), 2)
                # I compare the faces with our ids dictionary
                user_id, conf = recognizer.predict(greyscale[y:y + h, x:x + w])
                # I select a trust for the similitude between faces
                # WITH SMALL DATASETS THIS DOES NOT WORK WELL
                if conf < 70:
                    name = usernames_ids[user_id]
                else:
                    name = "unknown"
                cv2.putText(rectangle, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            cv2.imshow('img', img)
        # Press q for quitting the whole program
        # This decision was made because of a bug with my version of python in macOs, it's possible to
        # return instead of break
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
    crop_img = img[y:y + h, x:x + w]
    os.remove(image_path)
    cv2.imwrite(image_path, crop_img)
    return


def train_ai(path):
    # I have to create the cv2 face recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # Profile path of all of my instagram users
    prof_path = [os.path.join(path, user) for user in os.listdir(path)]
    # For learning the main idea is to have to dictionaries, one with [ids, usernames] and another one with
    # [[faces], ids] by this way
    faces = []
    ids = []
    usernames_ids = {}
    for user in prof_path:
        # necessary because of the creation of some temporal files
        if not os.path.isdir(user):
            continue
        user_path = [os.path.join(user, image) for image in os.listdir(user)]
        # random int for create an id
        internal_id = np.random.randint(0, 100000)
        usernames_ids[internal_id] = ('@' + user[12:])
        # Iterate over images
        for image in user_path:
            if ".jpg" in image:
                print(image)
                img = cv2.imread(image)
                greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # With numpy and the greyscale I convert the image into an array
                img_np = np.array(greyscale, 'uint8')
                # Append into an array of faces
                faces.append(img_np)
                ids.append(internal_id)
    # Now with  the array of images the module can work
    recognizer.train(faces, np.array(ids))
    recognizer.save('trained.yml')
    # I have to return the usernames_ids for the translation on the go with the webcam module
    return usernames_ids
