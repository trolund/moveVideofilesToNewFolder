import os
import shutil

oldpath = 'path with video'
newpath = r'new folder to move det video'

if not os.path.exists(newpath):
    os.makedirs(newpath)

for root, dirs, files in os.walk(oldpath):
        for file in files:
            if file.endswith(".avi") or file.endswith(".mkv") or file.endswith(".mp4"): # add or file.endswith(".mp4") for more fileformats
                print(os.path.join(root, file))
                if not os.path.exists(newpath + '/' + file):
                    shutil.move(os.path.join(root, file), newpath)
