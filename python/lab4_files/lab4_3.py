import glob
import sys
from datetime import datetime
from shutil import copyfile
from pathlib import Path

#uppg 3
#anrop: & "C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python37_64/python.exe" c:/Users/s_ola/Dropbox/Jobb/Scripting/kod/python/lab4_files.py -d 
# c:/Users/s_ola/Dropbox/Jobb/Scripting/kod/python -f *.txt

files = glob.glob(sys.argv[4])
print(f"Amount of text files in directory: {len(files)}")
for i in files: 
    print(i)
