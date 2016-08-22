from collections import OrderedDict

def extract(s2p,p2m,megaList):
    lastLine = len(megaList)-1
    lookout = [ '[Disease or Syndrome]',
                '[Neoplastic Process]',
                '[Finding]',
                '[Pathologic Function]',
                '[Acquired Abnormality]',
                '[Therapeutic or Preventive Procedure]',
                '[Functional Concept]',
                '[Spatial Concept]']
    combine_findings_with_contexts = []
    for k,v in p2m.items():
        done = False
        f0 = f1 = f2 = f3 = f4 = f5 = False
        g0 = g1 = g2 = g3 = g4 = g5 = False
        if len(v) !=0:
            for j in range(len(v)): # moving to different meta mappings
                if done:
                    break
                if j == len(v)-1: #last metamap
                    p = v[j] #  p = actual number of where metamaps are written
                    f0,findings0 = movingLastMetaMaps(p,lastLine,megaList,lookout,0,f0,s2p,k)
                    f1,findings1 = movingLastMetaMaps(p,lastLine,megaList,lookout,1,f1,s2p,k)
                    f2,findings2 = movingLastMetaMaps(p,lastLine,megaList,lookout,2,f2,s2p,k)
                    f3,findings3 = movingLastMetaMaps(p,lastLine,megaList,lookout,3,f3,s2p,k)
                    f4,findings4 = movingLastMetaMaps(p,lastLine,megaList,lookout,4,f4,s2p,k)
                    f5,findings5 = movingLastMetaMaps(p,lastLine,megaList,lookout,5,f5,s2p,k)
                    done = f0 or f1 or f2 or f3 or f4 or f5
                    combine_findings_with_contexts = combine_findings_with_contexts + findings0 + findings1 + findings2 \
                                                     + findings3 + findings4 + findings5
                else:
                    pstart = v[j]
                    pend = v[j+1]
                    g0,findings0 = movingConsecMetaMaps(pstart,pend,megaList,lookout,0,g0,s2p,k)
                    g1,findings1 = movingConsecMetaMaps(pstart,pend,megaList,lookout,1,g0,s2p,k)
                    g2,findings2 = movingConsecMetaMaps(pstart,pend,megaList,lookout,2,g0,s2p,k)
                    g3,findings3 = movingConsecMetaMaps(pstart,pend,megaList,lookout,3,g0,s2p,k)
                    g4,findings4 = movingConsecMetaMaps(pstart,pend,megaList,lookout,4,g0,s2p,k)
                    g5,findings5 = movingConsecMetaMaps(pstart,pend,megaList,lookout,5,g0,s2p,k)
                    done = g0 or g1 or g2 or g3 or g4 or g5
                    combine_findings_with_contexts = combine_findings_with_contexts + findings0 + findings1 + findings2 \
                                                     + findings3 + findings4 + findings5

    return combine_findings_with_contexts


def movingLastMetaMaps(p,lastLine,megaList,lookout,num,flag,s2p,phrasePointer):
    findings_with_contexts = []
    while p <= lastLine:
        if megaList[p][0:10] == 'Processing' or megaList[p] == '\n':
            if flag==False:
                return flag,[]
            else:
                return flag,findings_with_contexts
        st = megaList[p].strip()
        if lookout[num] in st:
            relevant_st = getString(st)
            if lookout[6] in megaList[p-1] or lookout[7] in megaList[p-1]:
                st = megaList[p-1].strip()
                context_st = getString(st)
            else:
                context_st = ''
            d = OrderedDict()
            d['finding'] = relevant_st
            d['context'] = context_st
            mainSentencePointer = [maink for maink, v in s2p.iteritems() if phrasePointer in v]
            mainSentence = getRightSentence(mainSentencePointer[0],megaList)
            d['sentence'] = mainSentence
            findings_with_contexts.append(d)
            flag = True
        p = p + 1
    if flag == False:
        return flag,[]
    else:
        return flag,findings_with_contexts


def movingConsecMetaMaps(pstart,pend,megaList,lookout,num,flag,s2p,phrasePointer):
    findings_with_contexts = []
    for p in range(pstart,pend):
        st = megaList[p].strip()
        if lookout[num] in st:
            relevant_st = getString(st)
            if lookout[6] in megaList[p-1] or lookout[7] in megaList[p-1]:
                st = megaList[p-1].strip()
                context_st = getString(st)
            else:
                context_st = ''
            d = OrderedDict()
            d['finding'] = relevant_st
            d['context'] = context_st
            mainSentencePointer = [maink for maink, v in s2p.iteritems() if phrasePointer in v]
            mainSentence = getRightSentence(mainSentencePointer[0],megaList)
            d['sentence'] = mainSentence
            findings_with_contexts.append(d)
            flag = True
    if flag == False:
        return flag,[]
    else:
        return flag,findings_with_contexts




def getString(s):
    start = s.index(' ')
    try:
        end = s.index('(')
    except:
        end = s.index('[')
    return s[start:end].strip()

def getRightSentence(q,megaList):
    s = megaList[q]
    start = s.index('\'')+1
    end = s.index('\n')-1
    return s[start:end].strip()

def parseImpressions(s):
    p = -1
    res= []
    for i in range(len(s)):
        if i == len(s) - 1:
            t = s[p + 1:i+1].strip()
            if len(t) > 3:
                res.append(t)
        elif s[i] == '.':
            t = s[p+1:i].strip()
            if len(t) > 3:
                res.append(t)
            p = i
    return res

def parsePhrases(phrases):
    res = []
    for each in phrases:
        t = parseImpressions(each)
        res = res + t
    return res