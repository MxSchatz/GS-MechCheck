#moving all the files from folder and subfolders to another folder

import os
import shutil

MAIN =r''
DIRS = r''

for root, subdirs, files in os.walk(DIRS):
	print ('root', root)
	print ('subdirs', subdirs)
	print ('files', files)
	for file in files:
		path = os.path.join(root, file)
		shutil.move(path, MAIN)