
import subprocess
import json as simplejson
print(simplejson.dumps("\"foo\bar"))


metaMapBinDir = '/home/shukla/Documents/WMC/backendStuff/MetaMap/public_mm/bin/'
wsdDir = metaMapBinDir + 'wsdserverctl'
skmDir = metaMapBinDir + 'skrmedpostctl'

# stop wsd
wsdOutput = subprocess.Popen([wsdDir, 'stop'], stdout=subprocess.PIPE)
#wsdOutput = subprocess.check_output([wsdDir, 'start'])

# stop skm
skmOutput = subprocess.Popen([skmDir, 'stop'], stdout=subprocess.PIPE)
#skmOutput = subprocess.check_output([skmDir, 'start'])
#print skmOutput