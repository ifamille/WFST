# coding=utf-8
import sys
import re
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
        if vocabulary in punctuation_without_pause:
            continue
        elif len(vocabulary)==1:
            matchPunctuation = re.match(r'^\W$', vocabulary, re.I|re.U|re.M)
            if matchPunctuation !=None:
                continue
            else:
                fw.write(vocabulary.encode('utf-8')+'\n')
        else:
            # use regular expression to extract possible number
            matchNum = re.match(r'^[0-9]+', vocabulary, re.I|re.U|re.M)
            # find vocabulary contains number, like 18ge
            if matchNum !=None:
                number = matchNum.group(0)
                # part of number
                fw.write(number.encode('utf-8')+'\n')
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
