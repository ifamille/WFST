# coding=utf-8
import sys
import re
import os

monophones0_iPath = '../voxforge/manual/monophones0'
oDirectory = '../voxforge/manual/autoGen/'
oFile_name = 'tree.hed_LR'
fmonophones = open(monophones0_iPath, 'r')
fTree_hed = open(oDirectory + oFile_name, 'w')
if os.path.exists(oDirectory):
    print('Loading...')
    phones = list(fmonophones)
    for phone in phones:
        if phone[:-1] != 'sil':
            fTree_hed.write('QS  ' + '\"R_' + phone[:-1] + '\"' + ' \t' + '{ ' + '*+' + phone[:-1] + ' }' + '\n')
    for phone in phones:
        if phone[:-1] != 'sil':
            fTree_hed.write('QS  ' + '\"L_' + phone[:-1] + '\"' + ' \t' + '{ ' +  phone[:-1] + '-*' + ' }' + '\n')
else:
    print('Wrong path!')

print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, new file ' + oFile_name + ' has been generated in ' + oDirectory + '.')
print('---------------------------------------')
fTree_hed.close()
fmonophones.close()
