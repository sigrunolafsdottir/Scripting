import argparse

parser = argparse.ArgumentParser()

#om jag inte anger a på kommandoraden, check_string_for_empty sätts som a:s värde
parser.add_argument("-a", nargs='?', default="check_string_for_empty")
args = parser.parse_args()

if args.a == "check_string_for_empty":
    print ("I can tell that no argument was given and I can deal with that here.")
elif args.a == "magic.name":
    print ("You nailed it!")
else:
    print (args.a)