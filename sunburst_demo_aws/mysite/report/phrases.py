# from pprint import pprint



def getSentence(s):
    start = 0
    if ":" in s:
        start = s.index(":")
    temp = s[start+1:]
    temp = temp.replace("\'","")
    temp = temp.replace("\n","")
    return temp.strip().title()

def getPhrase(s):
    i = 0
    start = s.index(":")
    temp = s[start + 1:]
    temp = temp.replace("\'", "")
    temp = temp.replace("\n", "")
    return temp.strip().title()

def getFinding(s):
    startRound = len(s)
    startSquare = len(s)
    start = s.index(' ')
    if '(' in s:
        startRound = s.index('(')
    if '[' in s:
        startSquare = s.index('[')

    if startRound < startSquare:
        end = startRound
    else:
        end = startSquare
    return s[start+1:end]

# Removed '[Functional Concept]',
#            '[Spatial Concept]'
#  '[Therapeutic or Preventive Procedure]',

def parse(opFile,accession,pole):
    fp = open(opFile,'r')
    megaList = []
    lookout = ['[Disease or Syndrome]',
               '[Neoplastic Process]',
               '[Pathologic Function]',
               '[Acquired Abnormality]',
               '[Injury or Poisoning]',
               '[Finding]',
               '[Anatomical Abnormality]'
               ]
    currentPhrase = None
    currentSentence = None
    for line in fp:
        if line != "\n":
            line = line.strip()
            megaList.append(line)

    # print megaList
    res = []
    findingSet = set()
    flag = False
    i = 0
    while i < (len(megaList)):
        if 'Processing' in megaList[i]:
            currentSentence = getSentence(megaList[i])
            i += 1
        elif 'Phrase:' in megaList[i]:
            currentPhrase = getPhrase(megaList[i])
            i += 1
        else:
            for j in range(len(lookout)):
                if lookout[j] in megaList[i]:
                    finding = getFinding(megaList[i]).strip().title()
                    if (lookout[j] == '[Finding]' and len(finding.split(' ')) < 2) \
                            or finding in ["Very Low","Pain Nos"] or \
                            'Nos' in finding or 'PLAN' in finding:
                        continue # # Edge case when '[Finding]' just contain one word
                    if finding not in findingSet:
                        findingSet.add(finding)
                        d = {}
                        d['sentence'] = currentSentence
                        d['phrase'] = currentPhrase
                        d['finding'] = finding
                        d['lookout'] = lookout[j]
                        d['accession'] = accession
                        d['colorcode'] = pole

                        res.append(d)
            #         while 'Processing' not in megaList[i] and 'Phrase:' not in megaList[i]:
            #             i += 1
            #             flag = True
            #             if i >= len(megaList):
            #                 break
            #         if flag:
            #             break
            # if flag:
            #     i -= 1
            #     flag = False
            i += 1

    '''
    See help.txt
    TODO: Remove duplicate findings
    TODO: Issues to be dealt with:
        - Repeated unnecessary findings - accession num 5604898
    TODO: If PLAN finding is due to Disease or Syndrome - add info within brackets . ex: 5610637
    TODO: better handling of duplicates : ex: 5611715, 5614398
    TODO: Assign priorities, if in the same phrase, we have a finding and disease or syndrome - prefer disease
    or syndrome
    '''


    # pprint(res)
    return res



