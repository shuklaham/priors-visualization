
'''
processing json
Author: Shukla
'''
'''
1. Progression of disease with increase in lymphadenopathy and bilateral adrenal nodules.
2. retroperitoneal edema , new small left effusion and new small-volume ascites. Soft tissue thickening
along the undersurface of the left diaphragm is stable from the recent exam but increased from older
studies and suspicious for peritoneal tumor.
3. Increase in subtle sclerosis in the superior half of the L2 vertebral body suspicious for metastasis
'''
import json
from pymetamap import MetaMap
import subprocess

from getMetaMapResults import getMetamapResults

def jsonProcessor(dt,data,metaMapBinDir):
    neg_pos = ['impression_negated','impression_positive']
    negativePhrases = []
    positivePhrases = []
    completeList = []
    positiveSentenceList = []
    negativeSentenceList = []
    presence_negatives = True
    presence_positives = True
    if len(data[0][neg_pos[0]]) == 0:
        presence_negatives = False
    if len(data[0][neg_pos[1]]) == 0:
        presence_positives = False

    if presence_negatives:
        s = data[0][neg_pos[0]]
        pos = []
        for ct in range(len(s)):
            if s[ct].isdigit() and s[ct+1] == '.':
                pos.append(ct)
        if len(pos) == 0:
            negativeSentenceList.append(s)
        else: # If its a numbered list
            for i in range(len(pos)):
                try:
                    start = pos[i]+2
                    end = pos[i+1]-3
                    negativeSentenceList.append(s[start:end+1])
                except:
                    start = pos[i]+2
                    negativeSentenceList.append(s[start:])

    if presence_positives:
        s = data[0][neg_pos[1]]
        pos = []
        for ct in range(len(s)):
            if s[ct].isdigit() and s[ct+1] == '.':
                pos.append(ct)
        if len(pos) == 0:
            negativeSentenceList.append(s)
        else: # if its numbered list
            for i in range(len(pos)):
                try:
                    start = pos[i]+2
                    end = pos[i+1]-3
                    positiveSentenceList.append(s[start:end+1])
                except:
                    start = pos[i]+2
                    positiveSentenceList.append(s[start:])

    #mm = MetaMap.get_instance('/home/shukla/Documents/WMC/backendStuff/MetaMap/public_mm/bin/metamap')
    if presence_negatives:
        negativeSentencesClean = [x.encode("ascii").strip() for x in negativeSentenceList]
        negativePhrases = getMetamapResults(negativeSentencesClean,metaMapBinDir)
        for i in range(len(negativePhrases)):
            negativePhrases[i]['date'] = dt
            negativePhrases[i]['colorCode'] = -1
    if presence_positives:
        positiveSentencesClean = [x.encode("ascii").strip() for x in positiveSentenceList]
        positivePhrases = getMetamapResults(positiveSentencesClean,metaMapBinDir)
        for i in range(len(positivePhrases)):
            positivePhrases[i]['date'] = dt
            positivePhrases[i]['colorCode'] = 1

    completeList = negativePhrases + positivePhrases

    nameJson = 'result'+dt+'.json'
    with open(nameJson, 'w') as fp:
        json.dump(completeList, fp)

    return completeList

