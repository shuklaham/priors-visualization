
import subprocess
from phrases import phrases
import os
import time


def getMetamapResults(sentences,metaMapBinDir):
    '''
    print file.read(5)2.
    file.close()
    return ['Yes','We can']
    #for line in file:
        #print line
    '''
    metaMapExec = metaMapBinDir + 'metamap'
    fileExists = False
    input_file = None
    if sentences is not None:
        input_file = open("temp_input", "w")
    if sentences is not None:
        ids = range(1,len(sentences)+1)
        for identifier, sentence in zip(ids, sentences):
            input_file.write('%r|%r\n' % (identifier, sentence))

        input_file.flush()
        #output_file = open("temp_output", "w")

    command = [metaMapExec,'--sldiID','--silent']
    command.append(input_file.name)
    #command.append(output_file.name)
# ['/home/shukla/Documents/WMC/backendStuff/MetaMap/public_mm/bin/metamap', '--sldiID', '/tmp/tmp3grliz', '/tmp/tmpoC_O9s']

    metamap_process = subprocess.Popen(command, stdout=subprocess.PIPE)
    #time.sleep(5)
    while fileExists == False:
        if os.path.isfile("temp_input.out"):
            fileExists = os.stat("temp_input.out").st_size != 0

    findings = phrases("temp_input.out")

    os.remove(input_file.name)
    os.remove("temp_input.out")


    return findings