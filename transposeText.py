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
    for vocabulary in vocabularyList:
        vocabulary = unicode(vocabulary,'utf-8')
        if len(vocabulary)==1:
            if vocabulary in punctuation_without_pause:
                continue
            else:
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
            # use regular expression to extract possible number
            matchNum = re.match(r'^[0-9]+(.)[0-9]*', vocabulary, re.I|re.U|re.M)
            # find vocabulary contains number, like 18ge
            if matchNum !=None:
                number = matchNum.group(0)
                # part of number
                numberInWord = numbers2Word(number)
                fw.write(numberInWord.encode('utf-8')+'\n')
                # part of hanzi
                fw.write(vocabulary[len(number):].encode('utf-8')+'\n')
            # didn't find vocabulary contains number.
            else:
                fw.write(vocabulary.encode('utf-8') + '\n')
print('---------------------------------------')
print('Executing...\n')
print('Congratuation, new file ' + file_name + ' has been generated.')
print('---------------------------------------')
fr.close()
fw.close()
