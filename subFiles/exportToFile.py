import os
import sys
import os.path

def titleWrite(n, s):
    saveLoc = open(s, 'w+')
    fWrite = saveLoc.write
    fWrite('Hash for file: ' + n + "\n")
    return s

def fileWrite(n, s):
    saveLoc = open(s, 'a+')
    prevData = saveLoc.read()
    fWrite = saveLoc.write
    fWrite(n + '\n')
    return s

