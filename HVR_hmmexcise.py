#######################################################################
#                                                                     #
#     This program takes an input hmm_file and an input fasta file.   # 
#     It outputs hmmscan data and a fasta file with all of the        #
#     excised domains.                                                #
#                                                                     #
#     Any accessions that did not hit an hmm from the file with a     #
#     Bit Score of 25.0 will be omitted and those accessions are      #
#     printed to stdout(the command line).                            #
#                                                                     # 
#     Command: python HVR_hmmexcise.py [hmm_file] [input_fasta]           #
#                                                                     #
#######################################################################


import argparse
import sys
import os
import re
import subprocess

def __main__():



######################################################################
#    Parsing command lines arguments. Input needs to be as below:    #
#                                                                    #
#    python HVR_hmmexcise.py [hmm_file] [input_fasta]                    #
######################################################################

    parser = argparse.ArgumentParser("Excises sequence with homology to HMM file")
    parser.add_argument('hmm_file', type=str)
    parser.add_argument('input_fasta', type=str)

    args = parser.parse_args()

#############################################################
#     Subprocessing to run hmmscan within the program       #
#                                                           #
#     This will output a .txt file that contains hmmscan    #
#     output.                                               #
#############################################################

    process = subprocess.Popen(['hmmscan', '-o' + args.input_fasta.split('.')[0] + '_hmmscan.txt' , args.hmm_file, args.input_fasta])
    process.wait()



    fileoutput = args.input_fasta.split('.')[0] + '_excised.txt'
    hmmscan_output = args.input_fasta.split('.')[0] + '_hmmscan.txt'

##############################################################
#     Opens hmmscan output file and reads the data. Splits   #
#     the file by query and accesses the top hmm hit.        #
#     Evaluates the BS of the match between each domain      #
#     and the hmm file and prints each domain that hits      #
#     the top hmm with Bit Score of at least 25              #
##############################################################

    hmmscanfile = open(hmmscan_output, 'r')
    FO = open(fileoutput, "w")
    HSO = re.split("Query:", hmmscanfile.read())[1:]

    i=0
    for query in HSO:
        lines = re.split("\n", query)
        accession = re.split(" +", lines[0])[1]
        hits = re.split(">+", query)
        if ">>" in query:

            HMMhit = re.split(" ", hits[1])[1]

            domains = re.split("==", hits[1])

            for domain in range(1, len(domains)):
                domainlines = re.split("\n\n", domains[domain])
                BitS = re.split(" ", domains[domain])[5]
                if float(BitS) < 10.0:
                    continue
                hmmsequence = ""
                sequence = ""
                HVRsequence = ""
                for line in range(1, len(domainlines)):
                    sublines = domainlines[line].split("\n")
                    if len(sublines) == 4:
                        hmmsequence += re.split(" +", sublines[0])[3]
                        sequence += re.split(" +", sublines[2])[3]
                        print(hmmsequence)
                HVRstart = hmmsequence.find("GhgaDelf")
                HVRend = hmmsequence.find("Pfldeel") + 4
                HVRsequence = sequence[HVRstart:HVRend].replace("-", "").upper()

                i+=1
                if len(HVRsequence) > 40:
                    FO.write(">"+accession+"_HVR\n"+HVRsequence+"\n")
                    #FO.write(accession+"\n")
        else:
            print(re.split(" +", lines[0])[1])





if __name__=="__main__":
    __main__()