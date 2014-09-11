# coding=utf-8
import sys
import re
import os

# original directory
word_directory = './PYWVox/'
intermediate_word_directory = './PYWs/'
# objective directory
pronunciation_directory = './PYPLs/'
intermediate_pronunciation_directory = './PYPs/'
destination_directory = './Components/'
# backup directory
backup_directory = './Backup/'
lexicon_name = 'voxforge_lexicon_part_2'
if os.path.exists(word_directory) and os.path.exists(pronunciation_directory):
    print('Loading...')
    file_list = ''
    # rescutive
    for file_or_folder in os.listdir(word_directory):
        # generate full file path which to be treated
        file_path = os.path.join(word_directory, file_or_folder)
        # generate full file path which to save the new file generated.
        name_extension = str(file_or_folder).split('.')
        name = str(name_extension[0])
        word_path = os.path.join(word_directory, name + '.pyw') 
        pronunciation_path = os.path.join(pronunciation_directory, name + '.pyp') 
        lexicon_path = os.path.join(destination_directory, name + '.tmp')
        # judge wheather one object in the directory is a file.
        if os.path.isfile(word_path) and os.path.isfile(pronunciation_path):
            # copy source file to intermediate_directory PYWs
            os.system("cp " + word_path + " " + intermediate_word_directory)
            # copy source file to intermediate_directory PYWs
            os.system("cp " + pronunciation_path + " " + intermediate_pronunciation_directory)
            # execute statement.
            os.system('paste -d " " ' + word_path + ' ' + pronunciation_path + ' > ' + lexicon_path)
            file_list += lexicon_path
            file_list += ' '
    os.system("cat " + file_list + " > " + destination_directory + lexicon_name)
    for file_or_folder in os.listdir(destination_directory):
        name_extension = str(file_or_folder).split('.')
        if len(name_extension)==2 and name_extension[1] == 'tmp':
            os.remove(os.path.join(destination_directory, file_or_folder))
else:
    print('Wrong path!')

print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, all the files in directory <PYVLs> have been transformed into ' + destination_directory +' directory.')
print('---------------------------------------')
