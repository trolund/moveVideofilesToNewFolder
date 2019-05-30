import os
import shutil
import sys

print("Searching for movies at:")
oldpath = sys.argv[1]
print(oldpath)
print("Moving files to:")
newpath = sys.argv[2]
print(newpath)

if not os.path.exists(newpath):
    os.makedirs(newpath)
    print(newpath + "dir created")

print("Files being moved:\n")
for root, dirs, files in os.walk(oldpath):
        for file in files:
            if file.endswith(".avi") or file.endswith(".mkv") or file.endswith(".mp4"): # add or file.endswith(".mp4") for more fileformats
                print(os.path.join(root, file))
                if not os.path.exists(newpath + '/' + file):
                    shutil.move(os.path.join(root, file), newpath)
