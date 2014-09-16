# coding=utf-8
# This script is to transpose the words in the text, for each word, it will keep one line, for each ponctuation, it will also keep one line.
import sys
import re
# convert number to word
def numbers2Word(numbers):
    parts = numbers.split('.')
    word = ''
    # in the case of integer
    # calculate amount of integer's bit
    bit = len(parts[0])
    #print(bit)
    zero = ''
    for i in range(bit):
        if parts[0][i] == '0':
            if bit-i==5:
                word+=bit2Word(bit-i)
                zero == ''
            else:
                zero = u'零'
                continue
        else:
            #print('bit='+str(bit)+', i='+str(i)+ ' element='+ parts[0][i])
            if i == bit-2:
                if parts[0][i]=='1' and parts[0][i+1]=='0':
                    word += zero
                    word += u'十'
                else:
                    word += zero
                    zero =''
                    word += number2Word(parts[0][i])+bit2Word(bit-i)
            elif bit == 6 and i==0 and parts[0][i]=='1':
                #print('shi')
                word += u'十'
            else:
                word += zero
                zero = ''
                word += number2Word(parts[0][i])+bit2Word(bit-i)
    if len(parts)==2:
        word += u'点'
        for j in range(len(parts[1])):
            word += number2Word(parts[1][j])
    return word
def fullwidth2Halfwidth(uBit):
    if uBit == u'\uff10':
        return number2Word('0') 
    elif uBit == u'\uff11':
        return number2Word('1')
    elif uBit == u'２':
        return number2Word('2')
    elif uBit == u'\uff13':
        return number2Word('3')
    elif uBit == u'\uff14':
        return number2Word('4')
    elif uBit == u'\uff15':
        return number2Word('5')
    elif uBit == u'\uff16':
        return number2Word('6')
    elif uBit == u'\uff17':
        return number2Word('7')
    elif uBit == u'\uff18':
        return number2Word('8')
    elif uBit == u'\uff19':
        return number2Word('9')

# convert bit to word, for example, 5 to wan, 4 to qian, 3 to bai
def bit2Word(bit):
    shi = [2,6]
    bai = [3,7]
    qian = [4,8]
    wan = [5]
    yi = [9]
    word = ''
    if bit == 1:
        word = ''
    elif bit in shi:
        word = u'十'
    elif bit in bai:
        word = u'百'
    elif bit in qian:
        word = u'千'
    elif bit in wan:
        word = u'万'
    elif bit in yi:
        word = u'亿'
    else:
        word = ''
    return word

# convert one number to word
def number2Word(number):
    if number == '0':
        word = u'零'
    elif number == '1':
        word = u'一'
    elif number == '2':
        word = u'二'
    elif number == '3':
        word = u'三'
    elif number == '4':
        word = u'四'
    elif number == '5':
        word = u'五'
    elif number == '6':
        word = u'六'
    elif number == '7':
        word = u'七'
    elif number == '8':
        word = u'八'
    else:
        word = u'九'
    return word

# read text file by console
iDirectory = '../../tmp/lm_segs/'
oDirectory = '../../tmp/lm_tts/'
rFile = open(iDirectory+sys.argv[1],'r')
# set the extension name as tt
name_extension = str(sys.argv[1]).split('.')
name = str(name_extension[0]) + '.tt'
wFile = open(oDirectory + name, 'w')
# load file
textList = list(rFile)
for text in textList:
    vocabularyList = text.split()
    # iterate each vocabulary
    for vocabulary in vocabularyList:
        vocabulary = unicode(vocabulary,'utf-8')
        # vocabuary has only one character, so may be a punctuation, a number or character.
        matchPunctuation = re.match(r'^[a-zA-Z]$', vocabulary[0], re.I|re.U|re.M)
        if matchPunctuation != None:
            continue
        if len(vocabulary)==1:
            # vocabulary is a punctuation in the list, ignore it
            # wheather it is not a character or number.
            matchPunctuation = re.match(r'^\W$', vocabulary, re.I|re.U|re.M)
            if matchPunctuation != None:
                #wFile.write(vocabulary.encode('utf-8')+'\n')
                wFile.write('\n')
            else:
                if vocabulary[0] >= u'\uff10' and vocabulary[0] <= u'\uff19':
                    wFile.write(fullwidth2Halfwidth(vocabulary[0]).encode('utf-8'))
                else:
                    # in the case of single number
                    matchSingleNum = re.match(r'^\d$', vocabulary, re.I|re.U|re.M)
                    if matchSingleNum != None:
                        vocabulary = number2Word(vocabulary)
                    wFile.write(vocabulary.encode('utf-8')+'\n')
        else:
            isNum = vocabulary[0] >='0' and vocabulary[0]<='9'
            number = ''
            if isNum:
                number += vocabulary[0]
            else:
                if vocabulary[0] >= u'\uff10' and vocabulary[0] <= u'\uff19':
                    wFile.write(fullwidth2Halfwidth(vocabulary[0]).encode('utf-8'))
                else:
                    wFile.write(vocabulary[0].encode('utf-8'))
            for c in range(1,len(vocabulary)):
                flag = vocabulary[c]=='.' or (vocabulary[c] >='0' and vocabulary[c]<='9')
                if isNum and flag:
                    number +=vocabulary[c]
                    if c == len(vocabulary)-1:
                        numberToWord = numbers2Word(number)
                        wFile.write(numberToWord.encode('utf-8'))
                elif not(isNum or flag):
                    if vocabulary[c] >= u'\uff10' and vocabulary[c] <= u'\uff19':
                        wFile.write(fullwidth2Halfwidth(vocabulary[c]).encode('utf-8'))
                    else:
                        wFile.write(vocabulary[c].encode('utf-8'))
                else:
                    if isNum:
                        if vocabulary[c]=='%':
                            pourcent = u'百分之'
                            wFile.write(pourcent.encode('utf-8'))
                            wFile.write('\n')
                            numberToWord = numbers2Word(number)
                            wFile.write(numberToWord.encode('utf-8'))
                        else:
                            numberToWord = numbers2Word(number)
                            wFile.write(numberToWord.encode('utf-8'))
                            wFile.write('\n')
                            wFile.write(vocabulary[c].encode('utf-8'))
                    else:
                        wFile.write('\n')
                        number = vocabulary[c]
                isNum = flag
            wFile.write('\n')

print('---------------------------------------')
print('Executing...\n')
print('Congratuation, new file ' + name + ' has been generated.')
print('---------------------------------------')
rFile.close()
wFile.close()
