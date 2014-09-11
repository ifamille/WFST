# coding=utf-8
import sys
import re
import os

destination_directory = './Components/'
lexicon_name = 'voxforge_lexicon_part_2'
news_name = 'voxforge_lexicon_part_1'
os.system("cat " + destination_directory + news_name + " " + destination_directory + lexicon_name + " > " + destination_directory +"lexicon.tmp")
print("cat " + destination_directory + news_name + " " + destination_directory + lexicon_name + " > " + destination_directory +"lexicon.tmp")
os.system("sort -u " + destination_directory + "lexicon.tmp > " + destination_directory + "voxforge_lexicon")
print("sort -u " + destination_directory + "lexicon.tmp > " + destination_directory + "voxforge_lexicon")
os.system("rm " + destination_directory + "lexicon.tmp")
print('---------------------------------------')
print('Executing ...\n')
print('Congratuation, new lexicon file ' + lexicon_name + ' has been generated in ' + destination_directory + ' directory.')
print('---------------------------------------')
#fr.close()
#fw.close()
