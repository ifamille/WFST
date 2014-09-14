# coding=utf-8
import sys
import re
import os

destination_directory = '../../data/'
phone_folder = '../../PYPLs/'
statistics_file = 'phone.sta'
os.system("cat " + phone_folder + "*.pyp" + " > " + destination_directory + "phones.tmp")
os.system("cat " + destination_directory + "phones.tmp" + " | tr -t [\" \"] [\"\\n\"] > " + destination_directory + "phone.tmp")
os.system("sort -u " + destination_directory + "phone.tmp > " + destination_directory + statistics_file)
print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, new lexicon file ' + statistics_file + ' has been generated in ' + destination_directory + ' directory.')
print('---------------------------------------')
#fr.close()
#fw.close()
