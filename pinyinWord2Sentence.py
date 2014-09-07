# coding=utf-8
import sys
# read .pyv file by console
fr = open(sys.argv[1],'r')
file_name = sys.argv[1].split('.')
file_name = file_name[0] + '.sent'
fw = open(file_name, 'w')
# load file
paragraphList = list(fr)
# deal with each line
for paragraph in paragraphList:
    words = paragraph.split()
    fw.write(' '.join(words))
    fw.write(' ')
print('---------------------------------------')
print('Executing...\n')
print('Congratuation, new file ' + file_name + ' has been generated.')
print('---------------------------------------')
fr.close()
fw.close()
