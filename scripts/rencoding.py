# coding=utf-8
# This script is to convert those texts encoded by gb2312 to utf-8.
import sys
import re
import os

oDirectory = '../law/'
iDirectory = '../law/'
oFile_name = 'rencoding.sh'
fw = open(oDirectory + oFile_name, 'w')
if os.path.exists(iDirectory) and os.path.exists(oDirectory):
    print('Loading...')
    for file_or_folder in os.listdir(iDirectory):
        file_path = os.path.join(iDirectory,file_or_folder)
        if os.path.isfile(file_path):
            name = str(file_or_folder).split('.')
            fw.write('iconv -f gb2312 -t UTF-8 ' + file_or_folder + ' > ' + '_' + name[0])
            fw.write('\n')

else:
    print('Wrong path!')

print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, new file ' + oFile_name + ' has been generated.')
print('---------------------------------------')
fw.close()
