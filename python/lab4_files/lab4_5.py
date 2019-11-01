import os
import glob
import sys
import argparse
import glob
from pathlib import Path
from shutil import copyfile
from datetime import datetime

#exempel anrop: C:\Users\s_ola\Dropbox\Jobb\Scripting\kod\python\lab4_files>
#  C:\Users\s_ola\AppData\Local\Programs\Python\Python36-32\python.exe 
# lab4_5argparse.py 
# C:/Users/s_ola/Dropbox/Jobb/Scripting/kod/python/dir1/output.txt 
# C:/Users/s_ola/Dropbox/Jobb/Scripting/kod/python/dir2/

parser = argparse.ArgumentParser(description='Filecopy')
parser.add_argument('srcDirAndFile')
parser.add_argument('destDir')

args = parser.parse_args()
print(args)

srcDirAndFile = args.srcDirAndFile
srcFile = os.path.basename(srcDirAndFile)
destDir = args.destDir
destDirFile = destDir+srcFile
ts = datetime.now().strftime('%Y%m%d%H%M%S')
pathMinusExtention, fileExtension = os.path.splitext(destDirFile)
newFilePathExistsTS = pathMinusExtention+ts+fileExtension

print(" ")
print("srcFile " + srcFile)
print("srcdirAndFile " + srcDirAndFile)
print("destDir " + destDir)
print("destDirFile " + destDirFile)
print("ts " + ts)
print("newFilePathExistsTS " + newFilePathExistsTS)
print(" ")
print("os.path.isdir(destDir) " + str(os.path.isdir(destDir)))
print("os.path.isfile(destDirFile) " + str(os.path.isfile(destDirFile)))
print("os.path.isfile(srcDirAndFile) " + str(os.path.isfile(srcDirAndFile)))
print(" ")


#kolla att dir och fil finns
#här finns filen i destDir, vi måste byta namn
if os.path.isdir(destDir) and os.path.isfile(destDirFile) and os.path.isfile(srcDirAndFile):   #finns redan, lägg på timestamp   
    print("kopierar fil från ", srcDirAndFile, " till ",newFilePathExistsTS)
    copyfile(srcDirAndFile, newFilePathExistsTS)

#destfolder finns men inte destfil, kopiera vanligt
elif os.path.isdir(destDir) and os.path.isfile(srcDirAndFile):  
    print("elif 1, verkar funka")
    print("kopierar fil från ", srcDirAndFile, " till ",destDirFile)
    copyfile(srcDirAndFile, destDirFile)

#ursprungliga filen finns, destdir måste skapas
elif os.path.isfile(srcDirAndFile): 
    print("elif 2")
    print("skapar dest dir ", destDir)
    os.makedirs(destDir)
    print("kopierar fil från ", srcDirAndFile, " till ",destDirFile)
    copyfile(srcDirAndFile, destDirFile)
else:
    print("Den fil du angav verkar inte existera")
    print("Kontrollera sökvägen och försök igen")



