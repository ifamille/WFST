# coding=utf-8
import sys
# read file
chinesePhoneWithTone = {'ā':'a1','á':'a2'}
f = open(sys.argv[1],'r')
wordList = list(f)
# read lines and execute treatment one by one
for word in wordList:
    # extract each syllable of one word
    syllables = word.split()
    for syllable in syllables:
        print(syllable)
        phone = list(syllable)
    print(chinesePhoneWithTone['á']+"\n"),
