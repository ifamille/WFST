# coding=utf-8
import sys
# read .pyv file by console
fr = open(sys.argv[1],'r')
file_name = sys.argv[1].split('.')
file_name = file_name[0] + '.pyw'
print(file_name + 'generated.')
fw = open(file_name, 'w')
# load file
wordList = list(fr)
# deal with each line
for word in wordList:
    syllables = word.split()
    for syllable in syllables:
        syllable = syllable.upper()
        fw.write(syllable)
    fw.write('\n')
fr.close()
fw.close()


