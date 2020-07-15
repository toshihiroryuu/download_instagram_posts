'''
------------------------------------------------------------------------------  
File name      : insta_downloader.py
Description    : Dowload all conetents from instagram
Python Version : 3.6.2
Copyright      : Open Source (MIT)
------------------------------------------------------------------------------
Version    Date          Author                  Remarks
1.0        15-July-2020  Athul Mathew            Created
------------------------------------------------------------------------------
'''

from instaloader import Instaloader
from instaloader import Profile

USERNAME = "**********"
PASSWORD = "**********"

# Get instance
L = Instaloader(download_video_thumbnails=False, 
                    download_comments=False, 
                    save_metadata=False, 
                    compress_json=False,
                    max_connection_attempts=10)

# Optionally, login or load session
L.login(USERNAME, PASSWORD)

followers_list = []

profile = Profile.from_username(L.context, USERNAME)

for follower in profile.get_followees():

    followers_list.append(follower.username)
    profile = Profile.from_username(L.context, follower.username)

    print("--------------------------", follower.username, "--------------------------")\

    for post in profile.get_posts():

        L.download_post(post, target = profile.username)

    print("--------------------------", profile.username, ": complete", "-------------")


