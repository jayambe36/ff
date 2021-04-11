import os
import shutil

TARGET = "LIVE_ff" # LIVE_DEMO is folder name

os.chdir(TARGET)

fileNames = os.listdir(".")

for file_ in fileNames:
	dirName = file_.split(".")[-1] # make folder 
	os.makedirs(dirName, exist_ok = True)
	src = file_ # rar,txt,png,jpg files sources
	dstn = os.path.join(dirName, file_) # folder like pdf,rar,txt,png,jpg merge wit respective files
	shutil.move(src, dstn) 