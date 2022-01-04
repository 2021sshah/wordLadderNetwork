# Siddharth Shah Gabor Pd.2
import time
import sys

def readFile(fileName, dctWrd, dctEdge):
    words = open(fileName, "r").readlines()
    edgeCount = 0
    for word in words:  # MAKE MORE EFFICIENT
        word = word.rstrip()
        dctWrd[word] = set()
        for nbr in neighbors(word): # LOOK UP TABLE
            if nbr in dctWrd and nbr != word:
                dctWrd[word].add(nbr)
                dctWrd[nbr].add(word)
                edgeCount += 1
    for word in dctWrd:
        size = len(dctWrd[word])
        if size not in dctEdge:
            dctEdge[size] = []
        dctEdge[size].append(word)
    return (len(words), edgeCount)

def neighbors(word):
    lnks, alpha = [], "abcdefghijklmnopqrstuvwxyz"
    for idx in range(len(word)):
        for ch in alpha:
            temp = "".join([word[:idx], ch, word[idx+1:]])
            lnks.append(temp)
    return lnks

def distribution(dctEdge):
    lent = max(dctEdge)
    val = dctEdge[lent]
    dctEdge.pop(lent)
    sndEx = dctEdge[max(dctEdge)][0]
    dctEdge[lent] = val
    lst = []
    for i in range(lent+1):
        if i not in dctEdge:
            dctEdge[i] = []
        lst.append(str(len(dctEdge[i])))
    return (", ".join(lst), sndEx)

def components(dctWrd):
    seen, arrayComp = set(), set()
    for word in dctWrd:
        if word not in seen:
            seen.add(word)
            parseMe = [word]
            for node in parseMe:
                for nbr in dctWrd[node]:
                    if nbr not in seen:
                        seen.add(nbr)
                        parseMe.append(nbr)
            if len(parseMe) not in arrayComp:
                arrayComp.add(len(parseMe))
    return (len(arrayComp), max(arrayComp))

def cliques(dctWrd):
    seen, numFreq = set(), [0,0,0]
    for word in dctWrd:
        if word not in seen:
            seen.add(word)
            lst = dctWrd[word]
            if len(lst) == 1:
                val = lst.pop()
                seen.add(val)
                if len(dctWrd[val]) == 1 and dctWrd[val] == {word}:
                    numFreq[0] += 1 
                lst.add(val)
            if len(lst) == 2:
                for nbr in lst:
                    seen.add(nbr)
                if len([nbr for nbr in lst if len(dctWrd[nbr]) == 2 and lst == (dctWrd[nbr] | {nbr}) - {word}]) == 2:
                    numFreq[1] += 1
            if len(lst) == 3:
                for nbr in lst:
                    seen.add(nbr)
                if len([nbr for nbr in lst if len(dctWrd[nbr]) == 3 and lst == (dctWrd[nbr] | {nbr}) - {word}]) == 3:
                    numFreq[2] += 1
    return numFreq


def farthest(start, dctWord):
    seen = {start}
    parseMe = [start]
    for word in parseMe:
        for nbr in dctWrd[word]:
            if nbr not in seen:
                seen.add(nbr)
                parseMe.append(nbr)
    return parseMe[-1]


def path(start, end, dctWord):
    dctSeen = {start: ""}
    if start == end:
        return pathFormat(start, dctSeen)
    parseMe = [start]
    for word in parseMe:
        for nbr in dctWrd[word]:
            if nbr not in dctSeen:
                dctSeen[nbr] = word
                if nbr == end:
                    return pathFormat(end, dctSeen)
                parseMe.append(nbr)
    return "-1"

def pathFormat(word, dctSeen):
    order, key = [], word
    while key:
        order.append(key)
        key = dctSeen[key]
    order = order[::-1]
    return ", ".join(order)

startTime = time.time()
dctWrd, dctEdge = {}, {}
stats = readFile(sys.argv[1], dctWrd, dctEdge)
print("Word Count: {}".format(stats[0]))
print("Edge Count: {}".format(stats[1]))
dist = distribution(dctEdge)
print("Degree List: {}".format(dist[0]))
midTime = time.time()
print("Construction Time: {}s".format(round(midTime-startTime, 3)))
if len(sys.argv) > 2:
    print("Second Degree Word: {}".format(dist[1]))
    comp = components(dctWrd)
    print("Connected Component Size Count: {}".format(comp[0]))   #Fix this!
    print("Largest Component Size: {}".format(comp[1]))
    clique = cliques(dctWrd)
    print("K2 Count: {}".format(clique[0]))
    print("K3 Count: {}".format(clique[1]))
    print("K4 Count: {}".format(clique[2]))
    print("Neighbors: {}".format(", ".join(dctWrd[sys.argv[2]])))
    print("Farthest: {}".format(farthest(sys.argv[2], dctWrd)))
    print("Path: {}".format(path(sys.argv[2], sys.argv[3], dctWrd)))
    print("Time Used: {}s".format(round(time.time()-startTime, 3)))