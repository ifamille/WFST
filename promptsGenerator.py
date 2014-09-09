# coding=utf-8
import sys
import re
import os

path = './ATs'
if os.path.exists(path):
    print('Loading...')
    for file_or_folder in os.listdir(path):
        print(file_or_folder)
        # judge wheather one object in the directory is a file.
        if os.path.isfile(os.path.join(path,file_or_folder)):
        else:
            print('NO')
else:
    print('Wrong path!')
## read text file by console
#fr = open(sys.argv[1],'r')
## set the extension name as tt
#file_name = str(sys.argv[1]) + '.tt'
#fw = open(file_name, 'w')
## load file
#textList = list(fr)

file_name = 'prompts'

print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, new file ' + file_name + ' has been generated.')
print('---------------------------------------')
#fr.close()
#fw.close()
