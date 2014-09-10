# coding=utf-8
import sys
import re
import os

path = './ATs'
file_name = 'prompts'
fw = open(file_name, 'w')
if os.path.exists(path):
    print('Loading...')
    for file_or_folder in os.listdir(path):
        full_path = os.path.join(path, file_or_folder)
        # judge wheather one object in the directory is a file.
        if os.path.isfile(full_path):
            fw.write('*/')
            f_name, f_extension = file_or_folder.split('.')
            fw.write(f_name+' ')
            ff = open(full_path, 'r')
            contents = list(ff)
            fw.write(contents[0])
            ff.close()
            fw.write('\n')
else:
    print('Wrong path!')
## read text file by console
#fr = open(sys.argv[1],'r')
## set the extension name as tt
#file_name = str(sys.argv[1]) + '.tt'
#fw = open(file_name, 'w')
## load file
#textList = list(fr)


print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, new file ' + file_name + ' has been generated.')
print('---------------------------------------')
#fr.close()
#fw.close()
