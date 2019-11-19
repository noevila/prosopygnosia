import os
import shutil

import prosopygnosia.artificial_intelligence.faces
from prosopygnosia.artificial_intelligence import ai_with_cv


def copy_images_from_path(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def just_crop(path):
    directory = os.listdir(path)
    for item in directory:
        prosopygnosia.artificial_intelligence.faces.number_of_faces(path + '/' + item)
    # I have to listdir again because of the deletions
    directory = os.listdir(path)
    for item in directory:
        prosopygnosia.artificial_intelligence.faces.crop_face(path + '/' + item)


def select_dataset():
    print("Please, select the number corresponding to the username of this dataset, if this user is not on this "
          "list type \"n\"")
    i = 0
    num_name = {}
    for name in os.listdir("./profiledata/"):
        if os.path.isdir("./profiledata/" + name):
            i += 1
            num_name[i] = name
            print(i, name)
    option = input(">>")
    while True:
        if option == "n":
            new_path = input("Introduce the new username: ")
            break
        elif int(option) in num_name:
            new_path = num_name[int(option)]
            break
        else:
            option = input("Please, introduce a valid option: ")
    return new_path
