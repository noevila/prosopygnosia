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
        for i, posts in enumerate(profile.get_posts()):
            # if i == NUMBER_OF_POSTS:
            #   break
            l.download_post(posts, profile_directory)


def copy_images_from_path(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def clean_and_crop(path):
    # Deletion f the jsons files
    directory = os.listdir(path)
    os.chdir(path)
    for subdirectory in directory:
        if not os.path.isdir(subdirectory):
            continue
        new_directory = os.listdir(subdirectory)
        for item in new_directory:
            if not item.endswith(".jpg"):
                os.remove(path + '/'+subdirectory+'/'+item)
            else:
                ai_with_cv.number_of_faces(path + '/'+subdirectory+'/'+item)
        # I have to listdir again because of the deletions
        new_directory = os.listdir(subdirectory)
        for item in new_directory:
            ai_with_cv.crop_face(path + '/'+subdirectory+'/'+item)


def main():
    l = instaloader.Instaloader()
    user = login(l)
    download(l, user)
    clean_and_crop('../profiledata')
    return
