# coding=utf-8
import sys
import re
import os

# original directory
seg_iDirectory = '../../tmp/lm_segs/'
# objective directory
tt_oDirectory = '../../tmp/lm_tts/'
pys_oDirectory = '../../tmp/lm_pyss/'
# backup directory
seg_bDirectory = '../../tmp/backup/'
if os.path.exists(seg_iDirectory) and os.path.exists(tt_oDirectory) and os.path.exists(pys_oDirectory):
    print('Loading...')
    # rescutive
    for seg_file in os.listdir(seg_iDirectory):
        # generate full file path which to be treated
        seg_file_path = os.path.join(seg_iDirectory, seg_file)
        # generate full file path which to save the new file generated.
        name_extension = str(seg_file).split('.')
        name = str(name_extension[0])
        tt_file_path = os.path.join(tt_oDirectory, name + '.tt') 
        # judge wheather one object in the directory is a file.
        if os.path.isfile(seg_file_path):
            # execute statement.
            os.system("python transposeText.py " + seg_file)
            # execute backcup and clean operations
            os.system("cp " + seg_file_path +" " + seg_bDirectory)
            os.system("touch " + pys_oDirectory + name + ".pys")
else:
    print('Wrong path!')

print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, all the files in directory <SEGs> have been transposed into ' + tt_oDirectory + ' directory.')
print('---------------------------------------')
