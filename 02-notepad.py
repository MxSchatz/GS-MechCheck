# tasks
#1. list out files in folder
#2. find mech folders with a file size
#3. move parent folders from step 2

# notes
# what about digital projects with out mechs?
# can you recognize digital projects?

import os
import shutil

#variables for server file paths 
MAIN =r''
DIRS = r''

#go to file path

for root, subdirs, files in os.walk(DIRS):
	print ('root', root)
	print ('subdirs', subdirs)
	print ('files', files)
#print directories with mechanicals

#find folder with mechanicals

#move root folder containing mechanicals to archive
