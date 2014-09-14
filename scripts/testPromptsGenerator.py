# coding=utf-8
# This script is to generate the test prompts. In fact, it only needs add */## in front of every transcription.
import sys
import re
import os

oDirectory = '../voxforge/test/'
iDirectory = '../voxforge/test/'
oFile_name = 'testprompts'
iFile_name = 'test_prompts'
fr = open(iDirectory + iFile_name, 'r')
fw = open(oDirectory + oFile_name, 'w')
if os.path.exists(iDirectory) and os.path.exists(oDirectory):
    print('Loading...')
    transcriptions = list(fr)
    for transcription in transcriptions:
        words = str(transcription).split()
        file_name = words[0]
        if len(file_name[:-1]) < 2:
            fw.write('*/Test_0' + file_name[:-1])
        else:
            fw.write('*/Test_' + file_name[:-1])
        fw.write(' ' + str(transcription)[len(file_name)+1:])
else:
    print('Wrong path!')

print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, new file ' + oFile_name + ' has been generated.')
print('---------------------------------------')
fw.close()
fr.close()
