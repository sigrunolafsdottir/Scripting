import os
import glob
import sys
from datetime import datetime
from shutil import copyfile
from pathlib import Path

#uppg 3
#anrop: & "C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python37_64/python.exe" c:/Users/s_ola/Dropbox/Jobb/Scripting/kod/python/lab4_files.py -d 
# c:/Users/s_ola/Dropbox/Jobb/Scripting/kod/python -f *.txt

#files = glob.glob(sys.argv[4])
#print(f"Amount of text files in directory: {len(files)}")
#for i in files: 
#    print(i)

#uppg 4
#amountOfPrints = int(sys.argv[2])
#filename = sys.argv[3]
#now = datetime.now().strftime('%Y%m%d %H:%M:%S')

#with open(filename, 'a') as file:
#    for x in range(0, amountOfPrints):
#        file.write(now + '\n')

#uppg 5
filename = sys.argv[1]
destDir = sys.argv[2]
destFile = sys.argv[3]
destDirFile = destDir+'/'+destFile
ts = datetime.now().strftime('%Y%m%d %H:%M:%S')+".txt"
destFileWithTimestamp = sys.argv[3]+datetime.now().strftime('%Y%m%d %H:%M:%S')+".txt"

if os.path.isfile(destDirFile):   #finns redan, lägg på timestamp
    copyfile(filename, destDirFileWithTimestamp)
else:
#    copyfile(filename, destDirFile)
    copyfile(filename, destDir+'/'+destFile)




