import glob
import os

#verkar bara funka om man står i det directory som programmet ligger i när man exekverar
#C:\Users\s_ola\Dropbox\Jobb\Scripting\kod\python\lab4_files>C:\Users\s_ola\AppData\Local\Programs\Python\Python36-32\python.exe lab4_2.py
print("in lab4_2")

files = glob.glob("*.txt")
files2 = glob.glob("*.*")
print(f"Amount of text files in directory: {len(files)}")
for i in files: 
    print(i)

print("printar *.*")
for i in files2: 
    print(i)