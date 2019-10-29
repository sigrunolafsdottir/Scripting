import os
import glob
import sys
from datetime import datetime
from shutil import copyfile
from pathlib import Path


#uppg 5, inte klar!!!
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




