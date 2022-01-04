# Siddharth Shah Gabor Pd.2
import time
import sys

def edges(words, word):
    lnks, alpha = [], "abcdefghijklmnopqrstuvwxyz"
    for idx in range(len(word)):
        for ch in alpha:
            temp = "".join([word[:idx], ch, word[idx+1:]])
            if temp != word and temp in words:
                lnks.append(temp[:-1])
    return lnks

startTime = time.time()
words = open(sys.argv[1], "r").readlines()  #Original File in List
dctWrd, edgeDist, edgeCount = {}, {}, 0     #Stores dct word with its array of neighbors, Stores dict edges with array of examples at degree, counts edges
for word in words:
    temp = edges(words, word)
    dctWrd[word] = temp
    if len(temp) not in edgeDist:
        edgeDist[len(temp)] = []
    edgeDist[len(temp)].append(word[:-1])
    edgeCount += len(temp)

print("Word count: {}".format(len(words)))
print("Edge Count: {}".format(edgeCount//2))
print("Degree List: ", end = "")
lim = max(edgeDist)
for i in range(lim+1):
    if i not in edgeDist:
        edgeDist[i] = []
    if i != lim:
        print("{},".format(len(edgeDist[i])), end = " ")
    else:
        print("{}".format(len(edgeDist[i])))
print("Construction Time: {}s\n".format(round(time.time()-startTime,1)))
