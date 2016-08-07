import json
from pprint import pprint
import difflib
from collections import  defaultdict
from helper import parseImpressions
from helper import parsePhrases

def getSentences(obj):
    # Extract data from json which is an array of json objects
    # dataFromApi = json.load(open('data/2952593482.json'))











    # Taking field "impression all" from json
    impressions_all = dataFromApi[0]["impression_all"][0]

    # Replacing all newline characters
    impressions_all = impressions_all.replace('\n',' ')

    # Parsing the main sentence list
    sentenceList = parseImpressions(impressions_all)

    print
    print 'All sentences'
    print
    for each in sentenceList:
        print each

    # Taking field "impression_negated" from json
    impression_negated = dataFromApi[0]["impression_negated"]

    # Replacing all newline characters
    impression_negated = [each.replace('\n',' ') for each in impression_negated]

    # Parsing the impression_negated phrases
    negatedPhrasesList = parsePhrases(impression_negated)



    # Compare each negative phrase with each in sentence list - its there according to difflib then add it to list
    #  of negative Sentences. Also record the indices of negative sentences selected so as to populate positive
    # sentence list
    recordNegations = defaultdict(int)
    negatedSentences = []
    postiveSentences = []

    for each in negatedPhrasesList:
        for i in range(len(sentenceList)):
            if each in sentenceList[i] or difflib.SequenceMatcher(None,sentenceList[i],each).ratio() > 0.95:
                negatedSentences.append(sentenceList[i])
                recordNegations[i] = 1
                break

    for i in range(len(sentenceList)):
        if recordNegations[i] == 0:
            postiveSentences.append(sentenceList[i])

    print
    print 'Negated sentences'
    print
    for each in negatedSentences:
        print each

    print
    print 'Positive sentences'
    print
    for each in postiveSentences:
        print each


# num_pos = []
# dot_pos = []
# sentenceList = []
# for ct in range(len(s)):
#     try:
#         if s[ct].isdigit() and s[ct + 1] == '.':
#             num_pos.append(ct)
#     except:
#         dummy = 0
#     if s[ct] == '.':
#         dot_pos.append(ct)
# if (len(num_pos) == 0 and len(dot_pos) == 1 and dot_pos[0] > 0.75 * len(s)) or (
#         len(num_pos) == 0 and len(dot_pos) == 0):
#     sentenceList.append(s)
# elif len(num_pos) == 0 and len(dot_pos) >= 1:  # handling sentences with just full stops
#     for i in range(len(dot_pos)):
#         if i == 0:
#             end = dot_pos[i]
#             sentenceList.append(s[0:end])
#         else:
#             start = dot_pos[i - 1]
#             end = dot_pos[i]
#             sentenceList.append(s[start + 1:end])
#     if dot_pos[-1] < len(s) - 1:
#         start = dot_pos[-1] + 1
#         sentenceList.append(s[start:])
# else:  # If its a numbered list
#     for i in range(len(num_pos)):
#         try:
#             start = num_pos[i] + 2
#             end = num_pos[i + 1] - 3
#             sentenceList.append(s[start:end + 1])
#         except:
#             start = num_pos[i] + 2
#             sentenceList.append(s[start:])
#
# print 'All sentences'
# for each in sentenceList:
#     print each
#
# # Get negative impressions
# negativePhrases = dataFromApi[0]["impression_negated"]
# negativeSentences = []
# postiveSentences = []
# recordNegatives = defaultdict(int)
#
# Compare each negative phrase with each in sentence list - its there according to difflib then add it to list
#  of negative Sentences. Also record the indices of negative sentences selected so as to populate positive
# sentence list
# for each in negativePhrases:
#     print each
#     for i in range(len(sentenceList)):
#         if difflib.SequenceMatcher(None,sentenceList[i],each).ratio() > 0.95:
#             negativeSentences.append(sentenceList[i])
#             recordNegatives[i] = 1
#             break
#
# for i in range(len(sentenceList)):
#     if recordNegatives[i] == 0:
#         postiveSentences.append(sentenceList[i])
#

# print 'Negative sentences'
# for each in negativeSentences:
#     print each
#
# print 'Positive sentences'
# for each in postiveSentences:
#     print each




