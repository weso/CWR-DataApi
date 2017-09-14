import codecs
import os
import sys
import getopt

from cwr.parser.decoder.file import default_file_decoder
from cwr.parser.encoder.cwrjson import JSONEncoder



if __name__ == '__main__':

    print(sys.version)
    print('CWR to JSON')

    inputfile = ''
    outputfile = ''
    argv = sys.argv[1:]
    try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
          print ('test.py -i <inputfile> -o <outputfile>')
          sys.exit(2)
    for opt, arg in opts:
          if opt == '-h':
             print ('test.py -i <inputfile> -o <outputfile>')
             sys.exit()
          elif opt in ("-i", "--ifile"):
             inputfile = arg
          elif opt in ("-o", "--ofile"):
             outputfile = arg

    #outputfile = "output/" +outputfile 
    print('\n')
    print('Reading file %s' % inputfile)
    print('Storing output on %s' % outputfile)
    print('\n')

    decoder = default_file_decoder()

    data = {}
    data['filename'] = os.path.basename(inputfile)
    lines  = codecs.open(inputfile, 'r', 'latin-1').readlines()
    data['contents'] = '';

    counter = 0
    counter2 = 0

    for line in lines :
        if line.startswith('COM') == False :
            data['contents'] += line
            counter2 +=1
            if counter2 == 35981 :
                print(line)
        else:
            counter +=1

    data['contents'] = data['contents'].replace('\n','')
    #replace '\r with 300 SPACES
    #this is needed inorder to be on the safe side to parse optional cwr params
    spaces =''
    for i in range(1,300):
      spaces +=" "
    spaces +='\n'
    data['contents'] = data['contents'].replace('\r',spaces)

    data = decoder.decode(data)
    encoder = JSONEncoder()
    result = encoder.encode(data)
    output = codecs.open(outputfile, 'w', 'latin-1')
    output.write(result)
