
def pickwod():
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
    print len(sortval)
