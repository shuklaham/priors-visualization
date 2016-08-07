from start import startParser
from pprint import pprint
import json

dataFromApi = json.load(open('data/sample.json'))
metaMapBinDir = '/home/shukla/Documents/WMC/backendStuff/MetaMap/public_mm/bin/'
j = startParser(dataFromApi,metaMapBinDir)

# pprint(j)
