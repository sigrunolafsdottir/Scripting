import argparse
import glob


#anrop: C:\Users\s_ola\Dropbox\Jobb\Scripting\kod\python\lab4_files>
# C:\Users\s_ola\AppData\Local\Programs\Python\Python36-32\python.exe 
# # lab4_3argparser.py -d "C:/Users/s_ola/Dropbox/Jobb/Scripting/kod/python/lab4_files/*"
# -f "*.txt"
parser = argparse.ArgumentParser()

parser.add_argument("-d", nargs='?', default="check_string_for_empty_dir", required=True)
parser.add_argument("-f", nargs='?', default="check_string_for_empty_filter", required=False)
args = parser.parse_args()
#default-filter
filter = "*"

#vi kollar om användaren har angivit ett filter
if args.f != "check_string_for_empty_filter":
    filter = args.f


if args.d == "check_string_for_empty_filter":
    print ("You did not supply a directory name")
else:
    filePath = args.d + filter
    folders = [f for f in glob.glob(filePath, recursive=False)]  
    print(f"Amount of text files in directory: {len(folders)}")
    for i in folders: 
        print(i)
