import cv2
import os

from prosopygnosia.artificial_intelligence.ai_with_cv import cascade

FACESPERUSER = 1000
cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')


def register_new_faces(new_user):
    os.mkdir(new_user)
    cwd = os.getcwd()
    os.chdir(new_user)
    i = 0
    # Initialization of the cv2 cam module
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
            for x in faces:
                if x.any():
                    i += 1
                    filename = str(i) + ".jpg"
                    cv2.imwrite(filename, img)
                    os.system('clear')
                    print("Please, move your face to get different angles")
                    print("Loading new face: ", i, "% saved...")
        if i == FACESPERUSER:
            break
    cam.release()
    cv2.destroyAllWindows()
    os.chdir(cwd)
    return()


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