# coding=utf-8
import sys
# read text file by console
fr = open(sys.argv[1],'r')
file_name = str(sys.argv[1]) + '.tt'
print('---------------------------------------')
print('Executing...\n')
print('New file ' + file_name + ' generated.')
print('---------------------------------------')
fw = open(file_name, 'w')
punctuation_without_pause=[u'“',u'”',u'-',u'《',u'》']
# load file
textList = list(fr)
for text in textList:
    vocabularyList = text.split()
    for vocabulary in vocabularyList:
        if vocabulary
        print(vocabulary)
    fw.write('\n')
fr.close()
fw.close()


