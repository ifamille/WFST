# coding=utf-8
import sys
import re
import os

# original directory
iDirectory = '../../tmp/lm_pyvs/'
# objective directory
oDirectory = '../../tmp/lm_pyws/'
# backup directory
bDirectory = '../../tmp/backup/'
if os.path.exists(iDirectory):
    print('Loading...')
    # rescutive
    for file_or_folder in os.listdir(iDirectory):
        # generate full file path which to be treated
        file_path = os.path.join(iDirectory, file_or_folder)
        # generate full file path which to save the new file generated.
        name_extension = str(file_or_folder).split('.')
        name = str(name_extension[0])
        destination_file_path = os.path.join(oDirectory, name + '.pyw') 
        # judge wheather one object in the directory is a file.
        if os.path.isfile(file_path):
            # execute statement.
            os.system("python pinyinVariant2Word.py " + file_or_folder)
            # execute backcup and clean operations
            os.system("cp " + file_path +" " + bDirectory)
            #os.system("rm " + file_path)
else:
    print('Wrong path!')

print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, all the files in directory <PYVs> have been transformed into ' + oDirectory + ' directory.')
print('---------------------------------------')
