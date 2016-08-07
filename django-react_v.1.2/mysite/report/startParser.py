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
import time
import re
import urllib2


# def startParser(obj,metaMapBinDir):
def startParser(mrn_id, acc_id):
	print 'Got mrn and acc, returning json now'
	# call Jai's api using mrn_id and acc_id
	obj = json.load(open('data/sample.json'))
	jLatest = obj[0]
	jsecondLatest = obj[1]
	jthirdLatest = obj[2]

	# metaMapBinDir
	metaMapBinDir = '/home/shukla/Documents/WMC/backendStuff/MetaMap/public_mm/bin/'

	#dates date[0] being latest
	dates = [obj[2]['finalized_time'][:10],obj[1]['finalized_time'][:10],obj[0]['finalized_time'][:10]]


	jsonObjects = [jthirdLatest,jsecondLatest,jLatest]

	commonFindings = set()
	processedJsonDict = OrderedDict()
	findingsDict = OrderedDict()

	'''
	processedJsonDict[date] looks like list following [{X - date, Y - Finding, Color code - (-1,0,1), Sentence}
	,{X - date, Y - Finding, Color code, Sentence},{X - date, Y - Finding, Color code, Sentence},
	{X - date, Y - Finding, Color code, Sentence}......]
	'''
	for i in range(len(dates)):
		processedJsonDict[dates[i]] = jsonProcessor(dates[i],jsonObjects[i],metaMapBinDir)

	# Make findings 'proper' and remove 'Identified' finding dictionary
	# start_time = time.clock()
	for d in dates:
		for i in range(len(processedJsonDict[d])):
			s = processedJsonDict[d][i]['finding']
			processedJsonDict[d][i]['finding'] = s.title()

	for d in dates:
		count = 0
		for point in processedJsonDict[d]:
			if point['finding'] == "Identified":
				del processedJsonDict[d][count]
			count+=1
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
			pointDict = {'finding':f,'context':'','sentence':'','date':d,'colorCode':'neutral'}
			processedJsonDict[d].append(pointDict)

	completeJson = []
	for d in processedJsonDict:
		completeJson += processedJsonDict[d]

	#append a Json object in common findings carrying all the extraInfo
	extraInfo = {}
	extraInfo['dates'] = dates
	extraInfo['all_findings'] = list(commonFindings)
	extraInfo['age']= jLatest["age"]
	extraInfo['technique_all'] = jLatest["technique_all"]
	extraInfo['patient_name'] = jLatest["patient_name"]
	extraInfo['acc_id'] = acc_id

	completeJson.append(extraInfo)
	print 'Prepared json. Pushing it to front-end'
	# resultName = str(acc_id)+'completeresult'+'.json'
	# with open(resultName, 'w') as fp:
	# 	json.dump(completeJson, fp)

	return completeJson

