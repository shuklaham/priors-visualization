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


def startParser(report_id):
	start_time = time.clock()

	# Initial settings
	# getting data
	dataDir = '/home/shukla/Documents/WMC/backendStuff/MetaMap/python-parser'

	#reading all three jsons
	response = urllib2.urlopen('http://localhost:8000/api/'+str(report_id)+'.json')
	dataFromApi = json.load(response)
	d1 = {}
	d1["impression_negated"] = dataFromApi["impressions_negated_date1"]
	d1["impression_positive"] = dataFromApi["impressions_positive_date1"]
	j1 = [d1]

	d2 = {}
	d2["impression_negated"] = dataFromApi["impressions_negated_date2"]
	d2["impression_positive"] = dataFromApi["impressions_positive_date2"]
	j2 = [d2]

	d3 = {}
	d3["impression_negated"] = dataFromApi["impressions_negated_date3"]
	d3["impression_positive"] = dataFromApi["impressions_positive_date3"]
	j3 = [d3]

	#dates
	dates = [dataFromApi['date1'],dataFromApi['date2'],dataFromApi['date3']]

	# j1 = json.loads(open('data/11-01-2015.json').read())
	# j2 = json.loads(open('data/09-01-2015.json').read())
	# j3 = json.loads(open('data/07-01-2015.json').read())


	metaMapBinDir = '/home/shukla/Documents/WMC/backendStuff/MetaMap/public_mm/bin/'

	#Start the server
	ps = subprocess.Popen(('ps', '-ef'), stdout=subprocess.PIPE)
	output = subprocess.check_output(('grep', 'java'), stdin=ps.stdout)
	if 'taggerserver' not in output:
		skrDir = metaMapBinDir + 'skrmedpostctl'
		skrOutput = subprocess.Popen([skrDir, 'start'], stdout=subprocess.PIPE)
		#wsdDir = metaMapBinDir + 'wsdserverctl'
		#skmOutput = subprocess.check_output([skmDir, 'start'])
		#print skmOutput

	# start wsd
	#wsdOutput = subprocess.Popen([wsdDir, 'start'], stdout=subprocess.PIPE)
	#wsdOutput = subprocess.check_output([wsdDir, 'start'])


	jsonObjects = [j1,j2,j3]

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
			#pointDict = ()
			pointDict = {'finding':f,'context':'','sentence':'','date':d,'colorCode':'neutral'}
			processedJsonDict[d].append(pointDict)

	completeJson = []
	for d in processedJsonDict:
		completeJson += processedJsonDict[d]

	#add dates at the end
	completeJson.append(dates)
	completeJson.append(list(commonFindings))

	resultName = 'completeresult_'+str(report_id)+'.json'

	# with open(resultName, 'w') as fp:
	# 	json.dump(completeJson, fp)

	# #closes server
	# metaMapBinDir = '/home/shukla/Documents/WMC/backendStuff/MetaMap/public_mm/bin/'
	# #wsdDir = metaMapBinDir + 'wsdserverctl'
	# skrDir = metaMapBinDir + 'skrmedpostctl'
    #
	# # stop skm
	# skrOutput = subprocess.Popen([skrDir, 'stop'], stdout=subprocess.PIPE)

	#skmOutput = subprocess.check_output([skmDir, 'start'])
	#print skmOutput

	# stop wsd
	#wsdOutput = subprocess.Popen([wsdDir, 'stop'], stdout=subprocess.PIPE)
	#wsdOutput = subprocess.check_output([wsdDir, 'start'])

	#print time.clock() - start_time
	# push above json
	return completeJson

