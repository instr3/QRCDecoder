import sys
from msl.loadlib import Client64
from zlib import decompress

def decode(filename):
    f=open(filename,'rb')
    bytes=f.read()
    f.close()
    if(bytes[:11]!=b'[offset:0]\n'):
        print('[Error] Unknown format for file %s'%filename)
        return ''
    client=Client64(module32='wrapper')
    result=client.request32('decrypt',bytes[11:])
    result=decompress(result)
    return str(result,encoding='utf-8')

if __name__ == '__main__':
    args=sys.argv
    if(len(args)<2):
        print('Usage: python main.py input_file.qrc')
    else:
        print(decode(args[1]),end='')