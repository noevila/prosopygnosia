import os
import shutil
from instaloader import instaloader, Profile
from prosopygnosia.artificial_intelligence import ai_with_cv

NUMBER_OF_POSTS = 3


def login(l):
    # Log in with user and create if it does not exists a session file.
    user = input("Introduce your username, without \"@\" ")
    if not os.path.isfile('./session' + user):
        l.interactive_login(user)
        l.save_session_to_file('./session' + user)
    else:
        l.load_session_from_file(user, './session' + user)
    return user


def download(l, user):
    # Download of the NUMBER_OF_POSTS photos for each of our followees
    personal_profile = Profile.from_username(l.context, user)
    target_profiles = personal_profile.get_followees()
    if not os.path.isdir('./profiledata'):
        os.mkdir('./profiledata')
    os.chdir('./profiledata')
    for profile in target_profiles:
        profile_directory = profile.username
        if os.path.isdir(profile_directory):
            continue
        else:
            os.mkdir(profile_directory)
            for i, posts in enumerate(profile.get_posts()):
                image_path = profile_directory + '/' + str(i)
                if posts.typename == 'GraphImage':
                    l.download_pic(image_path, posts.url, posts.date_local, filename_suffix=None, _attempt=1)
                elif posts.typename == 'GraphVideo':
                    continue
                elif posts.typename == 'GraphSidecar':
                    for j, node in enumerate(posts.get_sidecar_nodes()):
                        l.download_pic(image_path + str(j), node.display_url, posts.date_local,
                                       filename_suffix=None, _attempt=1)
        just_crop(profile_directory)
    os.chdir('../')


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
        ai_with_cv.number_of_faces(path + '/' + item)
    # I have to listdir again because of the deletions
    directory = os.listdir(path)
    for item in directory:
        ai_with_cv.crop_face(path + '/' + item)


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


def main():
    l = instaloader.Instaloader()
    user = login(l)
    download(l, user)
    return
