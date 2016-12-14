
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
#from pymetamap import MetaMap
import subprocess
import json
from pprint import pprint
import difflib
from collections import  defaultdict
from helper import parseImpressions
from helper import parsePhrases

from getMetaMapResults import getMetamapResults

def jsonProcessor(accession,jsonObject,metaMapBinDir):
    recordNegations = defaultdict(int)
    negatedSentences = []
    positiveSentences = []
    negativeDictPhrases = []
    positiveDictPhrases = []

    presence_negatives = True
    presence_positives = True

    if len(jsonObject["impression_negated"]) == 0:
        presence_negatives = False
    if len(jsonObject["impression_positive"]) == 0:
        presence_positives = False

    # Taking field "impression all" from json
    impressions_all = jsonObject["impression_all"][0]

    # Replacing all newline characters
    impressions_all = impressions_all.replace('\n', ' ')

    # Parsing the main sentence list
    sentenceList = parseImpressions(impressions_all)

    if presence_negatives:
        impression_negated = jsonObject["impression_negated"][0]

        # Replacing all newline characters
        impression_negated = impression_negated.replace('\n', ' ')

        # Parsing the impression_negated phrases
        negatedPhrasesList = parseImpressions(impression_negated)

    # Compare each negative phrase with each in sentence list - its there according to difflib then add it to list
    #  of negative Sentences. Also record the indices of negative sentences selected so as to populate positive
    # sentence list

    if presence_negatives:
        for each in negatedPhrasesList:
            for i in range(len(sentenceList)):
                if each in sentenceList[i] or difflib.SequenceMatcher(None, sentenceList[i], each).ratio() > 0.95:
                    negatedSentences.append(sentenceList[i])
                    recordNegations[i] = 1
                    break

    for i in range(len(sentenceList)):
        if recordNegations[i] == 0:
            positiveSentences.append(sentenceList[i])

    if presence_negatives and negatedSentences:
        negativeSentencesClean = [x.encode("ascii").strip() for x in negatedSentences]
        for i, each in enumerate(negativeSentencesClean):
            if each[-1] == "'":
                if each[0] == "'":
                    each = each[1:]
                negativeSentencesClean[i] = each[:len(each) - 1]
        negativeDictPhrases = getMetamapResults(negativeSentencesClean, metaMapBinDir, accession, 'neg')

    if presence_positives and positiveSentences:
        positiveSentencesClean = [x.encode("ascii").strip() for x in positiveSentences]
        for i, each in enumerate(positiveSentencesClean):
            if each[-1] == "'":
                if each[0] == "'":
                    each = each[1:]
                    positiveSentencesClean[i] = each[:len(each) - 1]
        positiveDictPhrases = getMetamapResults(positiveSentencesClean, metaMapBinDir, accession, 'pos')

    # if presence_negatives:
    #     negativeSentencesClean = [x.encode("ascii").strip() for x in negatedSentences]
    #     for i,each in enumerate(negativeSentencesClean):
    #         if each[-1] == "'":
    #             if each[0] == "'":
    #                 each = each[1:]
    #             negativeSentencesClean[i] = each[:len(each)-1]
    #     negativePhrases = getMetamapResults(negativeSentencesClean,metaMapBinDir)
    #     for i in range(len(negativePhrases)):
    #         negativePhrases[i]['accession'] = accession
    #         negativePhrases[i]['colorCode'] = "neg"
    #
    # if presence_positives:
    #     positiveSentencesClean = [x.encode("ascii").strip() for x in positiveSentences]
    #     for i, each in enumerate(positiveSentencesClean):
    #         if each[-1] == "'":
    #             if each[0] == "'":
    #                 each = each[1:]
    #                 positiveSentencesClean[i] = each[:len(each) - 1]
    #     positivePhrases = getMetamapResults(positiveSentencesClean,metaMapBinDir)
    #     for i in range(len(positivePhrases)):
    #         positivePhrases[i]['accession'] = accession
    #         positivePhrases[i]['colorCode'] = "pos"

    completeList = negativeDictPhrases + positiveDictPhrases

    # nameJson = 'result'+dt+'.json'
    # with open(nameJson, 'w') as fp:
    #     json.dump(completeList, fp)

    return completeList,sentenceList

