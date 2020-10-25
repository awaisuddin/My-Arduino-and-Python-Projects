import os
import time
import random
from os import listdir
from os.path import isfile, join
from random import randint
from InstagramAPI import InstagramAPI

PhotoPath = "C://Users//owais//Desktop//InstagramAutoposter//InstagramAutoposte//images"  # Change Directory to Folder with Pics that you want to upload
IGUSER = "dasaudiboi"  # Change to your Instagram USERNAME
PASSWD = "24491awais"  # Change to your Instagram Password
# Change to your Photo Hashtag
IGCaption = "Posyt byInstagramBot Awaz #coders #programming #programmer #programmingmemes #python #pycoders #javascript #java #csharp #programming #programmingmemes #programmer___humor #programmers_life #hacker #hacking #programminglife #programmerhumor"
os.chdir(PhotoPath)
ListFiles = sorted([f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))])
print(ListFiles)
print("Total Photo in this folder:" + str(len(ListFiles)))

# #Start Login and Uploading Photo
igapi = InstagramAPI(IGUSER, PASSWD)
igapi.login()  # login

for i, _ in enumerate(ListFiles):
    photo = "C://Users//owais//Desktop//InstagramAutoposter//InstagramAutoposte//images//1.jpeg"
    print("Now Uploading this photo to instagram: " + photo)
    igapi.uploadPhoto(photo, caption=IGCaption, upload_id=None)
    #os.remove(photo)
    # sleep for random between 60 - 120s
    n = randint(700,900)
    print("Sleep upload for seconds: " + str(n))
    time.sleep(n)
