import codecs
import os
import sys
import getopt
import io

from cwr.parser.decoder.file import default_file_decoder
from cwr.parser.encoder.cwrjson import JSONEncoder

#Read a cwr file stream via stdin and return back cwr-json via stdout
if __name__ == '__main__':

    decoder = default_file_decoder()

    data = {}
    data['filename'] = ''
    data['contents'] = '';

    for line in sys.stdin.readlines():
        #This is a workaround (still have some issues with COM record on some files)
        if line.startswith('COM') == False :
            data['contents'] += line
            if line.startswith('TRL') == True :
               break

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
    sys.stdout.write(result)
