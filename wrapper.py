from msl.loadlib import Server32
import ctypes

DES_KEYS=[
    [0x21, 0x40, 0x23, 0x29, 0x28, 0x4E, 0x48, 0x4C, 0x69, 0x75, 0x79, 0x2A, 0x24, 0x25, 0x5E, 0x26],
    [0x31, 0x32, 0x33, 0x5A, 0x58, 0x43, 0x21, 0x40, 0x23, 0x29, 0x28, 0x2A, 0x24, 0x25, 0x5E, 0x26],
    [0x21, 0x40, 0x23, 0x29, 0x28, 0x2A, 0x24, 0x25, 0x5E, 0x26, 0x61, 0x62, 0x63, 0x44, 0x45, 0x46]
]

class Wrapper(Server32):
    def __init__(self, host, port, quiet, **kwargs):
        super(Wrapper, self).__init__('lib/QQMusicCommon.dll','cdll', host, port, quiet)
        self.des=self.lib.__getattr__('?des@qqmusic@@YAHPAE0H@Z')
        self.ddes=self.lib.__getattr__('?Ddes@qqmusic@@YAHPAE0H@Z')
        self.keys=[bytes(x) for x in DES_KEYS]

    def decrypt(self,binary):
        result=ctypes.create_string_buffer(binary,len(binary))
        self.ddes(result,self.keys[0],len(result))
        self.des(result,self.keys[1],len(result))
        self.ddes(result,self.keys[2],len(result))
        return bytearray(result)
