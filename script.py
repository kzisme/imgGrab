import praw
import os
import requests
import urllib
from script_config import *

if not os.path.isfile("script_config.py"):
    print "You must create a config file for user + pass"
    exit(1)

user_agent = ("Top subreddit image grabber")
r = praw.Reddit(user_agent = user_agent)

r.login(REDDIT_USERNAME, REDDIT_PASS, disable_warning = True)

if not os.path.isfile("prev_imgs.txt"):
    prev_imgs = []
else:
    with open("prev_imgs.txt", "r") as f:
        prev_imgs = f.read()
        prev_imgs = prev_imgs.split("\n")

links = []
subreddit = r.get_subreddit('pics')
for submission in subreddit.get_top(limit = 25):
# Getting Username to add to mkdir
    newDirName = post.author.name

    if submission.id not in prev_imgs:
        #Download images...
        print "Links to be downloaded..."
        print submission.url
        links.append(submission.url)
        prev_imgs.append(submission.id)

i = 0
while os.path.exists('image%s.jpeg' % i):
    i += 1

for link in links:
    
        req = requests.get(link, stream = True)
        with open('image%s.jpeg' % i, 'wb') as f:
            i += 1
            f.write(req.content)



with open("prev_imgs.txt", "a") as f:
    for post_id in prev_imgs:
        f.write(post_id + "\n")
