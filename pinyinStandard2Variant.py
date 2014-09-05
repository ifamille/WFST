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
        #print(syllable)
        phone = list(unicode(syllable,'utf-8'))
        print(phone)
#        for phone in syllable:
#            if phone < 'a': 
#                print('tone<a'+'_'+phone),
#            elif phone > 'z':
#                print('tone>z'+'_'+phone),
#            else:
#                print('+'+phone),
        print('\n')
    print("\n")
