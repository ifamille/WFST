# coding=utf-8
import sys
# define tone dictionary
chinesePhoneWithToneDic = {'ā':'a1','á':'a2'}
chinesePhoneWithToneSet = []
# read file
f = open(sys.argv[1],'r')
# load lines
wordList = list(f)
# read lines and execute treatment one by one
for word in wordList:
    # extract syllables of one word
    syllables = word.split()
    # iterate each syllable of one word
    for syllable in syllables:
        phones = list(unicode(syllable,'utf-8'))
        for phone in phones:
            if phone > u'z':
                chinesePhoneWithToneSet.append(phone)
                print('_'+phone+'_'),
            else:
                print(phone),
        print('\n')
    print("\n")
