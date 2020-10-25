import os
import time
import random
from instabot import Bot
from os import listdir
from os.path import isfile, join
from random import randint

bot = Bot()
PhotoPath = "C://Users//owais//Desktop//InstagramAutoposter//InstagramAutoposte//images"  # Change Directory to Folder with Pics that you want to upload
IGUSER = "dasaudiboi"  # Change to your Instagram USERNAME
PASSWD = "24491awais"  # Change to your Instagram Password
# Change to your Photo Hashtag
IGCaption = "Posyt byInstagramBot Awaz #coders #programming #programmer #programmingmemes #python #pycoders #javascript #java #csharp #programming #programmingmemes #programmer___humor #programmers_life #hacker #hacking #programminglife #programmerhumor"
os.chdir(PhotoPath)
ListFiles = sorted([f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))])

for i, _ in enumerate(ListFiles):
    photo = ListFiles[i]
    print("Progress :" + str([i + 1]) + " of " + str(len(ListFiles)))
    print("Now Uploading this photo to instagram: " + photo)
    bot.login(username=IGUSER,password=PASSWD)
    bot.upload_photo(photo,caption=IGCaption)
    # os.remove(photo)
    # sleep for random between 60 - 120s
    n = 20
    print("Sleep upload for seconds: " + str(n))
    time.sleep(n)

    
    




