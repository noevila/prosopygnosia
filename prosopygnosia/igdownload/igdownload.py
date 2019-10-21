import os
from instaloader import instaloader, Profile

NUMBER_OF_POSTS = 20


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
    for profile in target_profiles:
        profile_directory = 'profiledata_' + profile.username
        for i, posts in enumerate(profile.get_posts()):
            if i == NUMBER_OF_POSTS:
                break
            l.download_post(posts, profile_directory)
        # Deletion f the jsons files (by now)
        dir_name = './' + profile_directory + '/'
        test = os.listdir(dir_name)
        for item in test:
            if not item.endswith(".jpg"):
                os.remove(os.path.join(dir_name, item))


def main():
    l = instaloader.Instaloader()
    user = login(l)
    download(l, user)
    return
