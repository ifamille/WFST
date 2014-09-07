# coding=utf-8
import sys
# define tone dictionary
tone_dic = {u'ā':'a1', u'á':'a2', u'ǎ':'a3', u'à':'a4', u'ō':'o1', u'ó':'o2', u'ǒ':'o3', u'ò':'o4', u'ē':'e1', u'é':'e2', u'ě':'e3', u'è':'e4', u'ī':'i1', u'í':'i2', u'ǐ':'i3', u'ì':'i4', u'ū':'u1', u'ú':'u2', u'ǔ':'u3', u'ù':'u4', u'ǘ':'v2', u'ǚ':'v3', u'ǜ':'v4'}
tone_set = []
# read file
f = open(sys.argv[1],'r')
file_name = sys.argv[1].split('.')
file_name = file_name[0] + '.ton'
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
               print('_' + tone_dic[phone] + '_'),
           else:
               print(phone),
        print('\n')
    print("\n")
for tone in tone_set:
    pen.write(tone.encode('utf-8'))
    pen.write('\n')
print('---------------------------------------')
print('Executing...\n')
print('Congratuation, new file ' + file_name + ' has been generated.')
print('---------------------------------------')
f.close()
pen.close()

