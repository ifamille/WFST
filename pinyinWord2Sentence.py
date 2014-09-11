# coding=utf-8
import sys
# read .pyv file by console
directory = './PYWs/'
destination_directory = './ATs/'
fr = open(directory + sys.argv[1],'r')
name_extension = sys.argv[1].split('.')
file_name = name_extension[0] + '.sent'
fw = open(destination_directory + file_name, 'w')
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
