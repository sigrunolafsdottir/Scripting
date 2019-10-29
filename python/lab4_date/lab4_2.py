import glob
import os


files = glob.glob("*.txt")
print(f"Amount of text files in directory: {len(files)}")
for i in files: 
    print(i)