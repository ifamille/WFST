# coding=utf-8
import sys
# read .pyv file by console
directory = './PYVs/'
destination_directory = './PYWs/'
fr = open(directory + sys.argv[1],'r')
name_extension = sys.argv[1].split('.')
file_name = name_extension[0] + '.pyw'
fw = open(destination_directory + file_name, 'w')
# load file
wordList = list(fr)
# deal with each line
for word in wordList:
    syllables = word.split()
    for syllable in syllables:
        syllable = syllable.upper()
        fw.write(syllable)
    fw.write('\n')
print('---------------------------------------')
print('Executing...\n')
print('Congratuation, new file ' + file_name + ' has been generated.')
print('---------------------------------------')
fr.close()
fw.close()


