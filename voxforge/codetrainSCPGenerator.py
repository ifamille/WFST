# coding=utf-8
import sys
import re
import os

path = './test/wav/'
destination_directory = './test/'
file_name = 'codetrain.scp'
file_name_beta = 'train.scp'
fw = open(destination_directory + file_name, 'w')
fw_beta = open(destination_directory + file_name_beta, 'w')
if os.path.exists(path):
    print('Loading...')
    for file_or_folder in os.listdir(path):
        wav_file = os.path.join(path, file_or_folder)
        f_name, f_extension = file_or_folder.split('.')
        # judge wheather one object in the directory is a file.
        if os.path.isfile(wav_file) and f_extension == 'wav':
            fw.write('./wav/' + str(file_or_folder))
            fw.write(' ')
            fw.write('./mfcc/' + str(f_name) + '.mfc')
            fw.write('\n')
            fw_beta.write('./mfcc/' + str(f_name) + '.mfc')
            fw_beta.write('\n')
else:
    print('Wrong path!')

print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, new file ' + file_name + ' has been generated.')
print('---------------------------------------')
fw.close()
fw_beta.close()
