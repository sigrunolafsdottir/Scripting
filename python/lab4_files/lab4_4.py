from datetime import datetime
import argparse

#anrop, exempel: C:\Users\s_ola\Dropbox\Jobb\Scripting\kod\python\lab4_files>
# C:\Users\s_ola\AppData\Local\Programs\Python\Python36-32\python.exe 
# # lab4_4.py -rows 10 "C:/Users/s_ola/Dropbox/Jobb/Scripting/kod/python/lab4_files/output.txt"

parser = argparse.ArgumentParser()
parser.add_argument('-rows', nargs='+', required=True)
args = parser.parse_args()


#uppg 4
amountOfPrints = int(args.rows[0])
filename = args.rows[1]
now = datetime.now().strftime('%Y%m%d %H:%M:%S')

#w för att filen ska rensas först, a för att appenda
with open(filename, "a") as file:
    for x in range(0, amountOfPrints):
        file.write(now + '\n')
