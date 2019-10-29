import os
import glob
import sys
from datetime import datetime
from shutil import copyfile
from pathlib import Path


#uppg 4
amountOfPrints = int(sys.argv[2])
filename = sys.argv[3]
now = datetime.now().strftime('%Y%m%d %H:%M:%S')

with open(filename, 'a') as file:
    for x in range(0, amountOfPrints):
        file.write(now + '\n')
