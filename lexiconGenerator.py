# coding=utf-8
import sys
import re
import os

word_directory = './PYWs/'
pronunciation_directory = './PYPs/'
destination_directory = './Components/'
lexicon_name = 'voxforge_lexicon_part_1'
if os.path.exists(word_directory) and os.path.exists(pronunciation_directory):
    print('Loading...')
    file_list = ''
    for file_or_folder in os.listdir(word_directory):
        name_extension = str(file_or_folder).split('.')
        word_path = os.path.join(word_directory, str(name_extension[0]) + '.pyw')
        pronunciation_path = os.path.join(pronunciation_directory, str(name_extension[0]) + '.pyp')
        new_path = os.path.join(destination_directory, str(name_extension[0]) + '.tmp')
        # judge wheather one object in the directory is a file.
        if os.path.isfile(word_path) and os.path.isfile(pronunciation_path):
            os.system('paste -d " " ' + word_path + ' ' + pronunciation_path + ' > ' + new_path)
            file_list += new_path
            file_list += ' '
    os.system("cat " + file_list + "i > " + destination_directory + lexicon_name)
    for file_or_folder in os.listdir(destination_directory):
        name_extension = str(file_or_folder).split('.')
        # judge wheather one object in the directory is a file.
        if len(name_extension)==2 and name_extension[1]=='tmp':
            os.remove(os.path.join(destination_directory, file_or_folder))
else:
    print('Wrong path!')
print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, new lexicon file ' + lexicon_name + ' has been generated in ' + destination_directory + ' directory.')
print('---------------------------------------')
#fr.close()
#fw.close()
