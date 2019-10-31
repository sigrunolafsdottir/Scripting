import argparse
import glob
import sys
from shutil import copyfile
from pathlib import Path

#anrop: C:\Users\s_ola\Dropbox\Jobb\Scripting\kod\python\lab4_files>
# C:\Users\s_ola\AppData\Local\Programs\Python\Python36-32\python.exe lab4_3argparser.py -f *.txt
parser = argparse.ArgumentParser()

parser.add_argument("-f", nargs='?', default="check_string_for_empty_filter")
args = parser.parse_args()

if args.f == "check_string_for_empty_filter":
    print ("You did not supply a file name")
else:
    files = glob.glob(args.f)
    print(f"Amount of text files in directory: {len(files)}")
    for i in files: 
        print(i)