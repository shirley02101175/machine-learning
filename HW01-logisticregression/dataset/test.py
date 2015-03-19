from __future__ import division
import re
from os import listdir
Filelist1 = listdir('hockey')
Filelist2 = listdir('baseball')
m1 = len(Filelist1)
m2 = len(Filelist1)
regEx = re.compile('\\W*')
counters = {}
L = []
Lb = []
wordcount = []
valc = []
for i in range(m1):
    filename = 'hockey/'+Filelist1[i]
    lines = open(filename).readlines()
    for line in lines:
        line = line.strip()
        listfromlines = regEx.split(line)
        L.extend(listfromlines)
newLh=[tok.lower() for tok in L if len(tok)>0]

for i in range(m2):
    filename = 'baseball/'+Filelist2[i]
    lines = open(filename).readlines()
    for line in lines:
        line = line.strip()
        listfromlines = regEx.split(line)
        Lb.extend(listfromlines)

newLb=[tok.lower() for tok in Lb if len(tok)>0]
newL = newLh+newLb
for item in newL:
    if item in counters:
        counters[item] += 1
    else:
        counters[item] = 1

sumofval=sum([counter for word, counter  in counters.items()])
sortval=sorted([(counter/sumofval,word) for word, counter in counters.items()],reverse =True)
for i in range(500):
    #print sortval[i][0]
    wordcount.append(sortval[i][0])
    valc .append(sortval[i][1])
print wordcount
print valc
#finalval = map(lambda counters[item]: counters[item]/sumofval, counters)
