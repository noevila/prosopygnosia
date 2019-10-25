import os
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
        # Deletion f the jsons files (by now)
        dir_name = './' + profile_directory + '/'
        directory = os.listdir(dir_name)
        for item in directory:
            if not item.endswith(".jpg"):
                os.remove(os.path.join(dir_name, item))
            else:
                ai_with_cv.number_of_faces(os.path.realpath(open('./' + profile_directory + '/' + item).name))
        # I have to listdir again because of the deletions
        directory = os.listdir(dir_name)
        for item in directory:
            ai_with_cv.crop_face(os.path.realpath(open('./' + profile_directory + '/' + item).name))


def main():
    l = instaloader.Instaloader()
    user = login(l)
    download(l, user)
    return
