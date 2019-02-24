#all rights reserved accordingly. Contact auther at edward.anguiano@edwardssite.com
import hashlib
import sys
import os
import os.path

#This is non-verbose. The program will run accordingly and release a message.
BLOCKSIZE=65536


def f(n):
    _h = hashlib.sha3_256()
    with open(n, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            _h.update(buf)
            H = _h.hexdigest()
            buf = afile.read(BLOCKSIZE)
        print('SHA3 256:  ' + H)
        return H

def s(n):
    _h = hashlib.sha256()
    buf = n.encode()
    _h.update(buf)
    H = _h.hexdigest()
    print('SHA3 256:  ' + H)
    return H
