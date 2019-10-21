import face_recognition
import os


def number_of_faces(image_path):
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    if not len(face_locations) == 1:
        os.remove(image_path)
    return

