from datetime import date
import glob
import os

d0 = date(2019, 10, 8)
d1 = date(2019, 12, 24)
delta = d1 - d0
print (delta.days)

files = glob.glob("*.txt")
print(f"Amount of text files in directory: {len(files)}")
for i in files: 
    print(i)
 


