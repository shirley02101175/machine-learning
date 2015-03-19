import re
import glob
import string
from numpy import *

regEx = re.compile('\\W*')
keyword = ['0', '1', '2', '3', '4', '5', '6', '7', 'ca', '8', 'hockey', '9', 'go', 'play', '10', 'baseball', '25', 'nhl', '11', '12', '15', 'teams', '16', '20', 'hit', '14', 'period', 'vs', '13', '55', '18', '30', 'l', '17', 'next', 'la', 'boston', 'toronto', 'runs', 'espn', 'goal', 'division', 'cup', '19', 'pit', 'detroit', 'gm', 'against', 'played', '24', 'det', 'pittsburgh', '21', '22', 'buffalo', 'braves', '26', 'leafs', '23', 'wings', 'night', 'rangers', 'power', 'bos', '28', 'pts', '27', '93', '03', 'st', 'playoff', 'playoffs', 'average', 'april', '02', 'andrew', 'chicago', 'montreal', 'day', 'tor', 'points', 'chi', 'morris', 'bruins', 'run', '33', 'maynard', '35', 'van', 'ball', '34', '31', 'pens', 'pitcher', 'cal', 'devils', 'pitching', 'ice', 'b', 'blues', '29', '38', '04', 'g', '40', '32', 'hitter', 'cmu', 'flyers', 'goals', 'coach', 'puck', 'sox', 'shots', 'canada', 'sharks', '37', 'pick', 'penguins', 'nyi', 'louis', 'hitting', 'cubs', 'nj', '92', 'clutch', 'university', 'stl', 'show', 'scoring', '36', 'que', 'pp', 'guys', 'islanders', 'al', 'stanley', 'kings', 'jets', 'buf', 'vancouver', 'shot', 'jays', 'career', 'base', 'mon', 'batting', 'minnesota', '39', 'ramsey', 'final', 'draft', 'city', 'giants', '91', '05', 'sabres', 'such', 'ahl', 'v', 'used', 'nyr', 'netcom', 'joseph', '60', 'lemieux', 'flames', 'sport', 'mets', 'calgary', 'beat', '42', 'winnipeg', 'round', 'quebec', 'paul', 'goalie', '66', 'coverage', 'work', '45', '01', 'its', 'gerald', '75', '54', '48', 'washington', '2nd', 'frank', '43', 'ny']

def docvector(dirname):
    k  = 0
    vector = []
    for i in dirname:
        vector.append([])
        content1 = []
        k += 1
        lines = open(i).readlines()
        for line in lines:
            line = line.strip()
            listfromlines = regEx.split(line)
            newL = [tok.lower() for tok in listfromlines if len(tok) > 0]
            content1.extend(newL)
        for item in keyword:
            vector[k-1].append(float(content1.count(item)))
        #vector.append('\t')
        if k%100 == 0:
            print k
    print k
    #print vector[10]
    return  vector

def sigmoid(inX):
    return 1.0/(1+exp(-inX))

def loadData(filevector):
    dataMat = []
    labelMat = []
    Mat = []
    dataMat = filevector
    print dataMat[3]
    if (filevector == keybase):
        for i in range(995):
            labelMat.append(1.0)
    else:
        for i in range(995):
            labelMat.append(0.0)
    #print shape(dataMat)
    return dataMat,labelMat

def regression(dataIn,labelIn):
    dataMatrix = mat(dataIn)
    labelMatrix = mat(labelIn).transpose()
    m,n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 100
    weights = ones((n,1))
    for k in range(maxCycles):
        h = sigmoid(dataMatrix*weights)
        error = (labelMatrix - h)
        weights = weights +alpha*dataMatrix.transpose()*error
    #print weights
    return weights
   
def classify(inX,weights):
    prob = sigmoid(sum(inX*weights))
    print prob
    if prob > 0.5: return 1.0
    else: return 0.0
        

if __name__ == '__main__':
    dirbaseball = glob.glob('./baseball/*')
    dirhockey = glob.glob('./hockey/*')
    keybase = docvector(dirbaseball)
    keybase2 = docvector(dirhockey)
   # print keybase2
    #print type(keybase2)
    dataArr1,labelArr1 = loadData(keybase)
    dataArr2,labelArr2 = loadData(keybase2)
    dataArr = dataArr1 + dataArr2
    labelArr = labelArr1 + labelArr2
    print shape(dataArr)
    weights = regression(dataArr,labelArr)
    inX =[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    classify(inX,weights)

    
    

    






        





