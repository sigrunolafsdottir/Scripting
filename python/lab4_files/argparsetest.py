import argparse

#anrop: C:\Users\s_ola\Dropbox\Jobb\Scripting\kod\python\lab4_files>
# C:\Users\s_ola\AppData\Local\Programs\Python\Python36-32\python.exe argparsetest.py -a magic.name

parser = argparse.ArgumentParser()

#om jag inte anger a på kommandoraden, check_string_for_empty sätts som a:s värde
parser.add_argument("-d", nargs='?', default="check_string_for_empty")
parser.add_argument("-a", nargs='?', default="check_string_for_empty")
args = parser.parse_args()

if args.a == "check_string_for_empty":
    print ("I can tell that no argument was given and I can deal with that here.")
elif args.a == "magic.name":
    print ("You nailed it!")
else:
    print (args.a)