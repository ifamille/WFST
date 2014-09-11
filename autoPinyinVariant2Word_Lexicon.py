# coding=utf-8
import sys
import re
import os

# original directory
directory = './PYVLs/'
intermediate_directory = './PYVs/'
# objective directory
destination_directory = './PYWLs/'
intermediate_destination_directory = './PYWs/'
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
        destination_file_path = os.path.join(destination_directory, name + '.pyw') 
        intermediate_file_path = os.path.join(intermediate_destination_directory, name + '.pyw') 
        # judge wheather one object in the directory is a file.
        if os.path.isfile(file_path):
            # copy source file to intermediate_directory PYSs
            os.system("cp " + file_path + " " + intermediate_directory)
            # execute statement.
            os.system("python pinyinVariant2Word.py " + file_or_folder)
            # execute backcup and clean operations
            # copy source file to backup directory
            os.system("cp " + file_path + " " + backup_directory + directory)
            # move result to destination directory
            os.system("mv " + intermediate_file_path + " " + destination_directory)
            # copy result to backup directory
            os.system("cp " + destination_file_path +" " + backup_directory + destination_directory)
            # delete source file from original directory
            # os.system("rm " + file_path)
            os.system("rm " + os.path.join(intermediate_directory, file_or_folder))
else:
    print('Wrong path!')

print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, all the files in directory <PYVLs> have been transformed into ' + destination_directory +' directory.')
print('---------------------------------------')
