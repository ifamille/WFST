# coding=utf-8
import sys
import re
# convert number to word
def numbers2Word(numbers):
    parts = numbers.split('.')
    word = ''
    # in the case of integer
    # calculate amount of integer's bit
    bit = len(parts[0])
    for i in range(bit):
        word += number2Word(parts[0][i])+bit2Word(bit-i)
    if len(parts)==2:
        word += u'点'
        for j in range(len(parts[1])):
            word += number2Word(parts[1][j])
    return word

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
fr = open(sys.argv[1],'r')
# set the extension name as tt
file_name = str(sys.argv[1]) + '.tt'
fw = open(file_name, 'w')
punctuation_without_pause=[u'“',u'”',u'-',u'《',u'》',u'·']
# load file
textList = list(fr)
for text in textList:
    vocabularyList = text.split()
    # iterate each vocabulary
    for vocabulary in vocabularyList:
        vocabulary = unicode(vocabulary,'utf-8')
        # vocabuary has only one character, so may be a punctuation, a number or character.
        if len(vocabulary)==1:
            #print('single syllable:'+vocabulary)
            # vocabulary is a punctuation in the list, ignore it
            # wheather it is not a character or number.
            matchPunctuation = re.match(r'^\W$', vocabulary, re.I|re.U|re.M)
            if matchPunctuation != None:
                continue
            else:
                # in the case of single number
                matchSingleNum = re.match(r'^\d$', vocabulary, re.I|re.U|re.M)
                if matchSingleNum != None:
                    vocabulary = number2Word(vocabulary)
                fw.write(vocabulary.encode('utf-8')+'\n')
        else:
            isNum = vocabulary[0] >='0' and vocabulary[0]<='9'
            number = ''
            if isNum:
                number += vocabulary[0]
            else:
                fw.write(vocabulary[0].encode('utf-8'))
            for c in range(1,len(vocabulary)):
                flag = vocabulary[c]=='.' or (vocabulary[c] >='0' and vocabulary[c]<='9')
                if isNum and flag:
                    number +=vocabulary[c]
                    if c == len(vocabulary)-1:
                        numberToWord = numbers2Word(number)
                        fw.write(numberToWord.encode('utf-8'))
                elif not(isNum or flag):
                    fw.write(vocabulary[c].encode('utf-8'))
                else:
                    if isNum:
                        if vocabulary[c]=='%':
                            pourcent = u'百分之'
                            fw.write(pourcent.encode('utf-8'))
                            fw.write('\n')
                            numberToWord = numbers2Word(number)
                            fw.write(numberToWord.encode('utf-8'))
                        else:
                            numberToWord = numbers2Word(number)
                            fw.write(numberToWord.encode('utf-8'))
                            fw.write('\n')
                            fw.write(vocabulary[c].encode('utf-8'))
                    else:
                        fw.write('\n')
                        number = vocabulary[c]
                isNum = flag
            fw.write('\n')


            #print('multi syllables: '+vocabulary)
            ## use regular expression to extract possible number
            #matchNum = re.match(r'\d+(\.)?\d*', vocabulary, re.I|re.U)
            ## find vocabulary contains number, like 18ge
            #if matchNum !=None:
            #    print('multi syllables - contains number: '+vocabulary)
            #    number = matchNum.group(0)
            #    print(number)
            #    ## part of hanzi
            #    #fw.write(vocabulary[0:len(vocabulary)-len(number)].encode('utf-8')+'\n')
            #    # part of number
            #    numberInWord = numbers2Word(number)
            #    fw.write(numberInWord.encode('utf-8')+'\n')
            ## didn't find vocabulary contains number.
            #else:
            #    print('multi syllables - not contains number: '+vocabulary)
            #    fw.write(vocabulary.encode('utf-8') + '\n')
print('---------------------------------------')
print('Executing...\n')
print('Congratuation, new file ' + file_name + ' has been generated.')
print('---------------------------------------')
fr.close()
fw.close()
