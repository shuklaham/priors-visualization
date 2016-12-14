
import subprocess
from phrases import parse
import os
import time
from shutil import copyfile
import random


def getMetamapResults(sentences,metaMapBinDir,accession,pole):
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

    RANDOM_SUFFIX_RANGE = 1000000
    SUFFIX = random.randint(0, RANDOM_SUFFIX_RANGE)
    INPUT_FILE_NAME = "sunburst_metamap_" + str(pole) + str(SUFFIX)
    if sentences is not None:
        input_file = open(INPUT_FILE_NAME, "w")
    if sentences is not None:
        ids = range(1, len(sentences) + 1)
        for identifier, sentence in zip(ids, sentences):
            input_file.write('%r|%r\n' % (identifier, sentence))

        input_file.flush()

    command = [metaMapExec, '--sldiID', '--silent']

    command.append(INPUT_FILE_NAME)

    command = ' '.join(command)
    subprocess.call(command, shell=True)

    # command.append(output_file.name)
    # ['/home/shukla/Documents/WMC/backendStuff/MetaMap/public_mm/bin/metamap', '--sldiID', '/tmp/tmp3grliz', '/tmp/tmpoC_O9s']

    # metamap_process = subprocess.Popen(command, stdout=subprocess.PIPE)

    # while fileExists == False:
    #     if os.path.isfile("temp_input.out"):
    #         fileExists = os.stat("temp_input.out").st_size != 0
    OUTPUT_FILE_NAME = INPUT_FILE_NAME + '.' + 'out'
    # opFilePath = '/tmp/'+OUTPUT_FILE_NAME
    resultDicts = parse(OUTPUT_FILE_NAME, accession, pole)

    os.remove(INPUT_FILE_NAME)
    os.remove(OUTPUT_FILE_NAME)

    return resultDicts