# coding=utf-8
# This script is to download automatically those laws' text on line.
import sys
import re
import os

download_to = '../law/'
file_name = 'autoDownloader.sh'
http_part_1 = sys.argv[1]
http_part_2 = sys.argv[2]
upper = sys.argv[3]
lower = sys.argv[4]
fw = open(download_to + file_name, 'w')
if os.path.exists(download_to):
    if upper[0]=='0':
        if lower[0]=='0':
            for count in range(int(upper[1]), int(lower[1])+1):
                if count < 10:
                    fw.write('wget ' + http_part_1 + '0' + str(count) + http_part_2)
                    fw.write('\n')
                else:
                    fw.write('wget ' + http_part_1 + str(count) + http_part_2)
                    fw.write('\n')

        else:
            for count in range(int(upper[1]), int(lower)+1):
                if count < 10:
                    fw.write('wget ' + http_part_1 + '0' + str(count) + http_part_2)
                    fw.write('\n')
                else:
                    fw.write('wget ' + http_part_1 + str(count) + http_part_2)
                    fw.write('\n')
    else:
        for count in range(int(upper), int(lower)+1):
            fw.write('wget ' + http_part_1 + str(count) + http_part_2)
            fw.write('\n')
else:
    print('Path not exists!')
fw.close()

