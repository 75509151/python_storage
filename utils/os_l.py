import os
import time


video_path = "/home/mm/var/"

for root, dirs, files in os.walk(video_path, topdown=False):
    for name in files:
        print "name: " + str(name)
        video = os.path.join(root, name)
        print "video: " + str(video)
        print "---------------------"
        time.sleep(2)
