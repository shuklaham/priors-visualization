
import subprocess
from phrases import phrases
import os
import time
from shutil import copyfile


def getMetamapResults(sentences,metaMapBinDir):

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

    command = [metaMapExec,'--sldiID','--silent','--prune 2']
    command.append(input_file.name)

    #command.append(output_file.name)
# ['/home/shukla/Documents/WMC/backendStuff/MetaMap/public_mm/bin/metamap', '--sldiID', '/tmp/tmp3grliz', '/tmp/tmpoC_O9s']

    metamap_process = subprocess.Popen(command, stdout=subprocess.PIPE)

    while fileExists == False:
        if os.path.isfile("temp_input.out"):
            fileExists = os.stat("temp_input.out").st_size != 0

    findings = phrases("temp_input.out")

    os.remove(input_file.name)
    os.remove("temp_input.out")


    return findings