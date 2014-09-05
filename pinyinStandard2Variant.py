# coding=utf-8
import sys
# define tone dictionary
tone_dic = {'ā':'a1','á':'a2'}
tone_set = []
# read file
f = open(sys.argv[1],'r')
file_name = sys.argv[1].split('.')
file_name = file_name[0] + '.ton'
print(file_name)
pen = open(file_name,'w')
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
               tone_set.append(phone)
               print('_' + phone + '_'),
           else:
               print(phone),
        print('\n')
    print("\n")
for tone in tone_set:
    pen.write(tone.encode('utf-8'))
    pen.write('\n')
f.close()
pen.close()

