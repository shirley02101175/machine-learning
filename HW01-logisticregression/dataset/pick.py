from __future__ import division
import re
import glob

filebaseball = glob.glob('./baseball/*')
filehockey = glob.glob('./hockey/*')
regEx = re.compile('\\W*')
all_lines = []
all_lines2 = []
wordlist = ['the', 'to', 'a', 'in', '0', 'and', 'i', 'of', '1', 'that', 'is', 's', 'for', 'it', '2', 'he', 'edu', 'from', 't', 'was', 'you', 'on', '3', 'have', 'this', '4', 'but', 'be', 'they', 'with', 'not', 'as', 'subject', 'at', 'are', '5', 'if', 're', 'game', '6', 'his', 'team', 'or', 'writes', 'can', '7', 'will', 'would', 'all', 'has', 'year', 'com', 'article', 'what', 'up', 'who', 'don', 'one', 'so', 'an', 'out', 'about', 'by', 'there', 'ca', 'games', '8', 'think', 'more', 'hockey', '9', 'no', 'when', 'just', 'like', 'had', 'than', 'get', 'go', 'players', 'good', 'we', 'my', 'last', 'me', 'first', 'their', 'do', 'time', 'play', 'm', 'been', '10', 'him', 'season', 'some', 'were', 'know', 'only', 'baseball', 'any', 'how', 'win', '25', 'well', 'd', 'two', 'see', 'cs', 'your', 'new', 'league', 'better', 'now', 'player', 'did', 'even', 'because', 'other', 'nhl', '11', 'them', 'over', 'then', 'should', 'after', 'best', '12', 'could', 'too', 'also', 'back', 'much', 'way', 'really', '15', 'which', 'won', 'teams', 'does', 'people', '16', '20', 'hit', 'fans', 'many', 'here', 'why', '14', 'off', 'say', 'years', 'going', 'right', 'most', 'period', 'into', 'make', 'very', 'let', 'vs', 'mike', '13', 'john', '55', 'got', '18', 'still', 'series', 'may', 'll', '30', 'l', '17', 'didn', 'am', 'next', 'la', 'boston', 'second', 'those', 'toronto', 'being', 'since', 'great', 'roger', 've', 'these', 'runs', 'espn', 'goal', 'division', '00', 'before', 'said', 'down', 'cup', 'fan', 'anyone', '19', 'pit', 'e', 'might', 'detroit', 'take', 'made', 'gm', 'c', '_', 'while', 'david', 'against', 'played', '24', 'where', 'det', 'pittsburgh', '21', '22', 'mark', 'point', 'buffalo', 'lot', 'braves', '26', 'same', 'home', 'leafs', 'never', 'bad', 'probably', 'again', '23', 'wings', 'give', 'little', 'doesn', 'third', 'red', 'lost', 'night', 'rangers', 'power', 'look', 'bos', '28', 'pts', 'sure', '27', '93', '03', 'st', 'playoff', 'come', 'playoffs', 'average', 'another', 'r', 'playing', 'big', 'three', 'long', '1993', 'april', '02', 'something', 'around', 'andrew', 'list', 'stats', 'least', 'chicago', 'dave', 'both', 'bob', 'san', 'montreal', 'day', 'line', 'tor', 'maybe', 'world', 'points', 'news', 'chi', 'mail', 'every', 'left', 'want', 'morris', 'ever', 'bruins', 'run', 'end', '33', 'guy', '1992', 'far', 'believe', 'steve', 'maynard', '35', 'van', 'though', 'cc', 'ball', '34', 'always', '31', 'pens', 'put', 'pitcher', 'net', 'cal', 'through', 'devils', 'pitching', 'ice', 'b', 'blues', 'remember', 'post', 'few', '29', 'us', 'pretty', '38', '04', 'p', 'name', 'score', 'g', 'blue', 'between', '50', 'during', '40', '32', 'hitter', 'cmu', 'flyers', 'actually', 'each', 'start', 'getting', 'goals', 'coach', 'puck', 'please', 'pitt', 'winning', 'sox', 'record', 'shots', 'canada', 'sharks', '37', 'pick', 'penguins', 'nyi', 'away', 'scored', 'o', 'louis', 'defense', 'hitting', 'scott', 'need', 'cubs', 'went', 'thanks', 'smith', 'thing', 'nj', 'j', '92', 'isn', 'enough', 'call', 'clutch', 'university', 'high', 'thought', 'stl', 'watch', 'someone', 'show', 'scoring', '36', 'que', 'pp', 'philadelphia', 'man', 'guys', 'islanders', 'help', 'came', 'york', 'number', 'al', 'stanley', 'mean', 'kings', 'jets', 'buf', 'vancouver', 'shot', 'gary', 'michael', 'jose', 'jays', 'top', 'reason', 'either', 'question', 'h', 'career', 'base', 'mon', 'batting', 'wasn', 'minnesota', 'however', 'gets', 'find', 'course', 'young', 'tell', 'seen', '39', 'ramsey', 'final', 'draft', 'city', 'major', 'giants', 'defensive', 'yes', 'wins', '91', 'w', 'total', '05', 'sabres', 'real', 'such', 'things', 'ahl', 'v', 'used', 'times', 'nyr', 'netcom', 'joseph', 'joe', '60', 'lemieux', 'flames', 'anything', 'behind', 'until', 'sport', 'mets', 'keep', 'calgary', 'beat', '42', 'winnipeg', 'past', 'old', 'round', 'quebec', 'paul', 'goalie', '66', 'sports', 'numbers', 'heard', 'coverage', 'bill', 'work', '45', '01', 'must', 'its', 'gerald', '75', '54', '48', 'yet', 'washington', 'rather', 'our', 'lead', '2nd', 'frank', 'able', '43', 'seems', 'ny']

for i in filebaseball:
    lines = open(i).readlines()
    for line in lines:
        line = line.strip()
        listfromlines = regEx.split(line)
        all_lines.extend(listfromlines)
newL = [tok.lower() for tok in all_lines if len(tok) > 0]

for i in filehockey:
    lines = open(i).readlines()
    for line in lines:
        line = line.strip()
        listfromlines = regEx.split(line)
        all_lines2.extend(listfromlines)
newL2 = [tok.lower() for tok in all_lines2 if len(tok) > 0]


wordbaseball = []
wordhockey = []
findword = []
for item in wordlist:
    wordbaseball.append(newL.count(item))
for item in wordlist:
    wordhockey.append(newL2.count(item))


for i in range(500):
    if (wordbaseball[i]/(wordhockey[i]+1) > 2 or wordbaseball[i]/(wordhockey[i]+1) < 0.5):
        findword.append(wordlist[i])
print len(findword)
print findword

    
