'''
initiation
Author: Shukla
'''

import subprocess
import json
import sys
from jsonProcessor import jsonProcessor
from subprocess import check_output
from collections import OrderedDict

metaMapBinDir = '/home/shukla/Documents/WMC/backendStuff/MetaMap/public_mm/bin/'
wsdDir = metaMapBinDir + 'wsdserverctl'
skmDir = metaMapBinDir + 'skrmedpostctl'

# start wsd
wsdOutput = subprocess.Popen([wsdDir, 'start'], stdout=subprocess.PIPE)
#wsdOutput = subprocess.check_output([wsdDir, 'start'])

# start skm
skmOutput = subprocess.Popen([skmDir, 'start'], stdout=subprocess.PIPE)
#skmOutput = subprocess.check_output([skmDir, 'start'])
#print skmOutput

# getting data
dataDir = '/home/shukla/Documents/WMC/backendStuff/MetaMap/python-parser'
#dates
dates = ['11-01-2015','09-01-2015','07-01-2015']

#reading all three jsons
j1 = json.loads(open('data/11-01-2015.json').read())
j2 = json.loads(open('data/09-01-2015.json').read())
j3 = json.loads(open('data/07-01-2015.json').read())

jsonObjects = [j1,j2,j3]

commonFindings = set()
processedJsonDict = {}
findingsDict = {}

'''
processedJsonDict[date] looks like list following [{X - date, Y - Finding, Color code - (-1,0,1), Sentence}
,{X - date, Y - Finding, Color code, Sentence},{X - date, Y - Finding, Color code, Sentence},
{X - date, Y - Finding, Color code, Sentence}......]
'''
for i in range(len(dates)):
	processedJsonDict[dates[i]] = jsonProcessor(dates[i],jsonObjects[i])

#closes server
wsdDir = metaMapBinDir + 'wsdserverctl'
skmDir = metaMapBinDir + 'skrmedpostctl'

# stop wsd
wsdOutput = subprocess.Popen([wsdDir, 'stop'], stdout=subprocess.PIPE)
#wsdOutput = subprocess.check_output([wsdDir, 'start'])

# stop skm
skmOutput = subprocess.Popen([skmDir, 'stop'], stdout=subprocess.PIPE)
#skmOutput = subprocess.check_output([skmDir, 'start'])
#print skmOutput



# Feed in all the finding phrases from processedJsonDict to findingDict[date] = ()
#CommonFindings set = Union of findingDict[date]
for d in dates:
	listofDetailedFindings = processedJsonDict[d]
	findingsDict[d] = set()
	for pointDict in listofDetailedFindings:
		findingsDict[d].add(pointDict['finding'])
	commonFindings = commonFindings | findingsDict[d]

#Pick one processedJsonDict[date]
#Get all findings in a set
#Subtract above from CommonFindings set and add the result in processedJsonDict[date]
# Repeat for other processedJsonDict[date]

for d in dates:
	diff = commonFindings - findingsDict[d]
	for f in diff:
		pointDict = OrderedDict()
		pointDict = ()
		pointDict = {'finding':f,'context':'','sentence':'','colorCode':0}
		processedJsonDict[d].append(pointDict)

completeJson = []
for d in processedJsonDict:
	completeJson += processedJsonDict[d]


with open('result.json', 'w') as fp:
    json.dump(completeJson, fp)

# push above json



'''
from pymetamap import MetaMap
mm = MetaMap.get_instance('/home/shukla/Documents/WMC/backendStuff/MetaMap/public_mm/bin/metamap')
sents = ['Multiple bilateral pulmonary nodules as described suspicious for metastatic disease in patient with history of renal cell carcinoma.']
concepts,error = mm.extract_concepts(sents,[1,2])
for concept in concepts:
	print concept
'''

