# coding=utf-8
import sys
import re
import os

hmmdefs_iPath = '../voxforge/manual/hmm0/hmmdefs'
proto_iPath = '../voxforge/manual/proto'
oDirectory = '../voxforge/manual/hmm0/'
oFile_name = 'hmmdefs_'
fHmmdefs = open(hmmdefs_iPath, 'r')
fProto = open(proto_iPath, 'r')
fw = open(oDirectory + oFile_name, 'w')
if os.path.exists(hmmdefs_iPath) and os.path.exists(proto_iPath):
    print('Loading...')
    phones = list(fHmmdefs)
    proto = list(fProto)
    proto.pop(0)
    proto.pop(0)
    for phone in phones:
        fw.write('~h ')
        fw.write('"' + phone[:-1] +'"')
        fw.write('\n')
        for hmm in proto:
            fw.write(hmm)
        fw.write('\n')
else:
    print('Wrong path!')

print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, new file ' + oFile_name + ' has been generated.')
print('---------------------------------------')
fw.close()
fProto.close()
fHmmdefs.close()
