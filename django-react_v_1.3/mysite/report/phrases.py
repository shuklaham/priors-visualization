
from collections import OrderedDict

import helper

def phrases(filename):
    #fl = open('sample-output.txt','r')
    fl = open(filename,'r')
    megaList = []
    for line in fl:
        megaList.append(line)
    fl.close()

    lastLine = len(megaList)-1
    s2p = OrderedDict() # sentences to phrases mapping
    p2m = OrderedDict() # phrases to metamaps mapping



    # We are creating a mapping of indexes of processing to phrases -> senetences to phrases
    # take care if phrase is like 'and' or its last phrase
    for i in range(len(megaList)):
        if megaList[i][0:10] == 'Processing':
            s2p[i] = []
            currentSentencePointer = i
        if megaList[i][0:6] == 'Phrase':
            currentPhasePointer = i
            s2p[currentSentencePointer].append(currentPhasePointer)




    for k,v in s2p.items():
        if len(v) > 0:
            for i in range(len(v)):
                if i == len(v)-1: #last phrase
                    p2m[v[i]] = []
                    j = v[i]
                    while j <= lastLine:
                        if megaList[j][0:10] == 'Processing':
                            break
                        if megaList[j][0:12] == 'Meta Mapping':
                            p2m[v[i]].append(j)
                        j = j+ 1
                else:  #not last phrase
                    p2m[v[i]] = []
                    for j in range(v[i]+1,v[i+1]):
                        if megaList[j][0:12] == 'Meta Mapping':
                            p2m[v[i]].append(j)


    findings_with_contexts = helper.extract(s2p,p2m,megaList)

    return findings_with_contexts


