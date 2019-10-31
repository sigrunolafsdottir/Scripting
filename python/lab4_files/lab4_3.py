import glob
import sys
from shutil import copyfile
from pathlib import Path

#uppg 3
#anrop från VC: & "C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python37_64/python.exe" c:/Users/s_ola/Dropbox/Jobb/Scripting/kod/python/lab4_files.py -d 
# c:/Users/s_ola/Dropbox/Jobb/Scripting/kod/python -f *.txt (här måste vi kolla index 4)
#anrop från kommandoraden C:\Users\s_ola\Dropbox\Jobb\Scripting\kod\python\lab4_files>C:\Users\s_ola\AppData\Local\Programs\Python\Python36-32\python.exe lab4_3.py -f *.txt
#kommandoraden: vi kollar index 2

print (sys.argv)
files = glob.glob(sys.argv[2])

print(f"Amount of text files in directory: {len(files)}")
for i in files: 
    print(i)
