import os
from instaloader import instaloader, Profile
from prosopygnosia.instagram_and_os.os_functions import just_crop

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


def main():
    l = instaloader.Instaloader()
    user = login(l)
    download(l, user)
    return
