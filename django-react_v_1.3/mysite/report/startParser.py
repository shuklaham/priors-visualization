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
from operator import itemgetter


# def startParser(obj,metaMapBinDir):
def startParser(mrn_id, acc_id):
	print 'Got mrn and acc, returning json now'
	# call Jai's api using mrn_id and acc_id
	obj = json.load(open('data/sample_one_report.json'))

	jsonObjects = []
	timestamp_accession_list = []
	for each in obj:
		jsonObjects.append(each)
		temp = (each['finalized_time'],each['accession'])
		timestamp_accession_list.append(temp)

	# Sorted dates and accordingly accession numbers list
	timestamp_accession_list = sorted(timestamp_accession_list,key=itemgetter(0))
	timestamps,accession_nums = zip(*timestamp_accession_list)
	timestamps = list(timestamps)
	accession_nums = list(accession_nums)


	# jLatest = obj[0]
	# jsecondLatest = obj[1]
	# jthirdLatest = obj[2]

	# metaMapBinDir
	metaMapBinDir = '/home/shukla/Documents/WMC/backendStuff/MetaMap/public_mm/bin/'

	#dates date[0] being latest
	# dates = [obj[2]['finalized_time'],obj[1]['finalized_time'][:10],obj[0]['finalized_time'][:10]]

	# jsonObjects = [jthirdLatest,jsecondLatest,jLatest]

	commonFindings = set()
	processedJsonDict = OrderedDict()
	findingsDict = OrderedDict()

	'''
	processedJsonDict[date] looks like list following [{X - date, Y - Finding, Color code - (-1,0,1), Sentence}
	,{X - date, Y - Finding, Color code, Sentence},{X - date, Y - Finding, Color code, Sentence},
	{X - date, Y - Finding, Color code, Sentence}......]
	'''
	for i in range(len(accession_nums)):
		processedJsonDict[accession_nums[i]] = jsonProcessor(accession_nums[i],jsonObjects[i],metaMapBinDir)

	# Make findings 'proper' and remove 'Identified' finding dictionary
	# start_time = time.clock()
	for d in accession_nums:
		for i in range(len(processedJsonDict[d])):
			s = processedJsonDict[d][i]['finding']
			processedJsonDict[d][i]['finding'] = s.title()

	for d in accession_nums:
		count = 0
		for point in processedJsonDict[d]:
			if point['finding'] == "Identified":
				del processedJsonDict[d][count]
			count+=1
	# Feed in all the finding phrases from processedJsonDict to findingDict[date] = ()
	#CommonFindings set = Union of findingDict[date]
	for d in accession_nums:
		listofDetailedFindings = processedJsonDict[d]
		findingsDict[d] = set()
		for pointDict in listofDetailedFindings:
			findingsDict[d].add(pointDict['finding'])
		commonFindings = commonFindings | findingsDict[d]

	#Pick one processedJsonDict[date]
	#Get all findings in a set
	#Subtract above from CommonFindings set and add the result in processedJsonDict[date]
	# Repeat for other processedJsonDict[date]

	for d in accession_nums:
		diff = commonFindings - findingsDict[d]
		for f in diff:
			pointDict = OrderedDict()
			pointDict = {'finding':f,'context':'','sentence':'','accession':d,'colorCode':'neutral'}
			processedJsonDict[d].append(pointDict)

	completeJson = []
	for d in processedJsonDict:
		completeJson += processedJsonDict[d]

	#append a Json object in common findings carrying all the extraInfo
	extraInfo = {}
	extraInfo['timestamps'] = timestamps
	extraInfo['accession_nums'] = accession_nums
	extraInfo['all_findings'] = list(commonFindings)
	extraInfo['age']= jsonObjects[0]["age"]
	extraInfo['technique_all'] = jsonObjects[0]["technique_all"]
	extraInfo['patient_name'] = jsonObjects[0]["patient_name"]
	# extraInfo['acc_id'] = acc_id

	completeJson.append(extraInfo)
	print 'Prepared json. Pushing it to front-end'
	# resultName = str(acc_id)+'completeresult'+'.json'
	# with open(resultName, 'w') as fp:
	# 	json.dump(completeJson, fp)

	return completeJson

