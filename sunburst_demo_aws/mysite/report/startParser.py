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
from pprint import pprint


# def startParser(obj,metaMapBinDir):
# def startParser(mrn_id, acc_id):
def startParser(report_id):
	# print 'Got mrn and acc, returning json now'
	# call Jai's api using mrn_id and acc_id
	# obj = json.load(open('sample_one_report.json'))

	response = urllib2.urlopen('http://52.32.196.43:8000/api/'+str(report_id)+'.json')
	print 'Now here'
	data = json.load(response)
	# pprint(data)

	dates = []
	accessions = []
	jsonObjects = []

	count = 0
	for i in range(1,4):
		if not data['date'+str(i)]:
			break
		dates.append(data['date'+str(i)])
		accessions.append(data['accession'+str(i)])
		d = {}
		d['impression_all'] = [data['impression_all'+str(i)]]
		d['impression_negated'] = [data['impressions_negated_date'+str(i)]]
		d['impression_positive'] = [data['impressions_positive_date'+str(i)]]
		jsonObjects.append(d)
		count += 1
	# jLatest = obj[0]
	# jsecondLatest = obj[1]
	# jthirdLatest = obj[2]

	# metaMapBinDir
	metaMapBinDir = '/home/ubuntu/backend/MetaMap/public_mm/bin/'
	# Start the server
	ps = subprocess.Popen(('ps', '-ef'), stdout=subprocess.PIPE)
	for x in ps.stdout:
		if re.search("taggerserver", x):
			flag = True
	flag = False
	if not flag:
		skrDir = metaMapBinDir + 'skrmedpostctl'
		skrOutput = subprocess.Popen([skrDir, 'start'], stdout=subprocess.PIPE)

	# wsdDir = metaMapBinDir + 'wsdserverctl'
	# skmOutput = subprocess.check_output([skmDir, 'start'])
	# print skmOutput

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
	impresssionArray = []
	for i in range(len(accessions)):
		processedJsonDict[accessions[i]],sentenceList = jsonProcessor(accessions[i],jsonObjects[i],metaMapBinDir)
		res = ''
		# for j in range(len(sentenceList)-1):
		# 	res += sentenceList[j] + '<br>' + '<br>'
		# impresssionArray.append(res)
	# Make findings 'proper' and remove 'Identified' finding dictionary
	# start_time = time.clock()
	for d in accessions:
		for i in range(len(processedJsonDict[d])):
			s = processedJsonDict[d][i]['finding']
			processedJsonDict[d][i]['finding'] = s.title()

	for d in accessions:
		count = 0
		for point in processedJsonDict[d]:
			if point['finding'] == "Identified":
				del processedJsonDict[d][count]
			count+=1
	# Feed in all the finding phrases from processedJsonDict to findingDict[date] = ()
	#CommonFindings set = Union of findingDict[date]
	for d in accessions:
		listofDetailedFindings = processedJsonDict[d]
		findingsDict[d] = set()
		for pointDict in listofDetailedFindings:
			findingsDict[d].add(pointDict['finding'])
		commonFindings = commonFindings | findingsDict[d]

	#Pick one processedJsonDict[date]
	#Get all findings in a set
	#Subtract above from CommonFindings set and add the result in processedJsonDict[date]
	# Repeat for other processedJsonDict[date]

	for d in accessions:
		diff = commonFindings - findingsDict[d]
		for f in diff:
			pointDict = OrderedDict()
			pointDict = {'finding':f,'context':'','sentence':'','accession':d,'colorcode':'neutral'}
			processedJsonDict[d].append(pointDict)

	completeJson = []
	for d in processedJsonDict:
		completeJson += processedJsonDict[d]

	#append a Json object in common findings carrying all the extraInfo
	extraInfo = {}
	extraInfo['timestamps'] = dates
	extraInfo['accessions'] = accessions
	extraInfo['all_findings'] = list(commonFindings)
	extraInfo['clinical_statement'] = data["clinical_statement"]
	extraInfo['patient_name'] = data["name"]
	extraInfo['mrn'] = data["mrn"]
	for i,each in enumerate(jsonObjects):
		extraInfo["impression_all"+str(i)] = each['impression_all']

	completeJson.append(extraInfo)
	# print 'Prepared json. Pushing it to front-end'
	# resultName = str(report_id)+'completeresult'+'.json'
	# with open(resultName, 'w') as fp:
	# 	json.dump(completeJson, fp)

	return completeJson

if __name__=='__main__':
	startParser(1)
