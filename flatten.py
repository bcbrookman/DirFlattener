import shutil
import os

start_path = "/home/brian/testdir/"

for subdir in os.listdir(path=start_path):
    for root, dirs, files, in os.walk(os.path.join(start_path, subdir)):
        if root != os.path.join(start_path, subdir):
            for file in files:
                try:
                    shutil.move(os.path.join(root, file), os.path.join(start_path, subdir))
                except shutil.Error:    # if the file already exists in the destination directory
                    new_filename = str(root).replace("\\", "_").replace("/", "_").replace(" ", "-") + "_" + file
                    os.rename(src=os.path.join(root, file), dst=os.path.join(root, new_filename))
                    shutil.move(os.path.join(root, new_filename), os.path.join(start_path, subdir))

    for root, dirs, files, in os.walk(os.path.join(start_path, subdir)):
        for directory in dirs:
            shutil.rmtree(os.path.join(root, directory))
