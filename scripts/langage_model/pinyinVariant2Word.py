# coding=utf-8
import sys
import re
import os
# read .pyv file by console
iDirectory = '../../tmp/lm_pyvs/'
oDirectory = '../../tmp/lm_pyws/'
bDirectory = '../../tmp/backup/'
fr = open(iDirectory + sys.argv[1],'r')
name_extension = sys.argv[1].split('.')
oFile_name = name_extension[0] + '.pyw'
fw = open(oDirectory + oFile_name, 'w')
os.system('cp ' + iDirectory + name_extension[0] + '.pyv' + ' ' + bDirectory)
# load file
wordList = list(fr)
isEnterBefore = False
# deal with each line
for word in wordList:
    matchSyllables = re.match(r'^[a-z]$', word[0], re.I|re.U|re.M)
    # It is a special symbole
    if matchSyllables == None:
        # There isn't a enter symbole before.
        if not isEnterBefore:
            fw.write('\n')
            isEnterBefore = True
            continue
        # There is a enter symbole before.
        else:
            isEnterBefore = True
            continue
    else:
        isEnterBefore = False
    syllables = word.split()
    for syllable in syllables:
        syllable = syllable.upper()
        fw.write(syllable)
    fw.write('\n')
print('---------------------------------------')
print('Executing...\n')
print('Congratuation, new file ' + oFile_name + ' has been generated.')
print('---------------------------------------')
fr.close()
fw.close()


