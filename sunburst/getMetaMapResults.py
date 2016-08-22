import subprocess
from phrases import phrases
import os
import time
from shutil import copyfile
import random

def getMetamapResults(sentences,metaMapBinDir):

    metaMapExec = metaMapBinDir + 'metamap'
    fileExists = False
    input_file = None

    RANDOM_SUFFIX_RANGE =  1000000
    SUFFIX = random.randint(0, 1000000)

    if sentences is not None:
        input_file = open("/tmp/sunburst_metamap_%d" % SUFFIX, "w")
    if sentences is not None:
        ids = range(1,len(sentences)+1)
        for identifier, sentence in zip(ids, sentences):
            input_file.write('%r|%r\n' % (identifier, sentence))

        input_file.flush()

    command = [metaMapExec,'--sldiID','--silent']
    command.append(input_file.name)

    metamap_process = subprocess.Popen(command, stdout=subprocess.PIPE)

    output_file_name = "/tmp/sunburst_metamap_%d.out" % SUFFIX
    while fileExists == False:
        if os.path.isfile(output_file_name):
            fileExists = os.stat(output_file_name).st_size != 0

    findings = phrases(output_file_name)

    os.remove(input_file.name)
    os.remove(output_file_name)


    return findings