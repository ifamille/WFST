# coding=utf-8
import sys
import re
import os

directory = './OTs/'
destination_directory = './TTs/'
backup_directory = './Backup/'
if os.path.exists(directory):
    print('Executing...')
    for file_or_folder in os.listdir(directory):
        file_path = os.path.join(directory, file_or_folder)
        destination_file_path = os.path.join(destination_directory, file_or_folder+'.tt') 
        # judge wheather one object in the directory is a file.
        if os.path.isfile(file_path):
            os.system("sh ./Stanford/segment.sh ctb " + file_path +" utf8 0 > " + destination_file_path)
            os.system("cp " + file_path +" " + backup_directory + directory)
            os.system("cp " + destination_file_path +" " + backup_directory + destination_directory)
            os.system("rm " + file_path)
else:
    print('Wrong path!')

print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, all the files in directory <OTs> have been segmented.')
print('---------------------------------------')
