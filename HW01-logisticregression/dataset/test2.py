from __future__ import division
import re
import glob

filename = glob.glob('./*/*')
regEx = re.compile('\\W*')
all_lines = []
counters = {} 
for i in filename:
    lines = open(i).readlines()
    for line in lines:
        line = line.strip()
        listfromlines = regEx.split(line)
        all_lines.extend(listfromlines)
newL = [tok.lower() for tok in all_lines if len(tok)>0]

for item in newL:
    if item in counters:
        counters[item] += 1
    else:
        counters[item] = 1

sortval=sorted([(counter,word) for word, counter in counters.items()],reverse =True)

word  = []
count = []
for i in range(500):
    word.append(sortval[i][1])
for i in range(500):
    count.append(sortval[i][0])
print word,count
