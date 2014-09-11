# coding=utf-8
import sys
import re
import os

# original directory
directory = './PYSs/'
# objective directory
destination_directory = './PYVs/'
# backup directory
backup_directory = './Backup/'
if os.path.exists(directory):
    print('Loading...')
    # rescutive
    for file_or_folder in os.listdir(directory):
        # generate full file path which to be treated
        file_path = os.path.join(directory, file_or_folder)
        # generate full file path which to save the new file generated.
        name_extension = str(file_or_folder).split('.')
        name = str(name_extension[0])
        destination_file_path = os.path.join(destination_directory, name + '.pyv') 
        # judge wheather one object in the directory is a file.
        if os.path.isfile(file_path):
            # execute statement.
            os.system("python pinyinStandard2Variant.py " + file_or_folder)
            # execute backcup and clean operations
            os.system("cp " + file_path +" " + backup_directory + directory)
            os.system("cp " + destination_file_path +" " + backup_directory + destination_directory)
            os.system("rm " + file_path)
else:
    print('Wrong path!')

print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, all the files in directory <PYSs> have been transformed into ' + destination_directory +' directory.')
print('---------------------------------------')
