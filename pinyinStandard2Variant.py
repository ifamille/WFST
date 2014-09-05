import sys

f = open(sys.argv[1],'r')
wordList = list(f)
for word in wordList:
    print(word),