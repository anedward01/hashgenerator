import os
import sys
import os.path
import datetime

def titleWrite(n, s):
    date = datetime.datetime.now()
    saveLoc = open(s, 'w+')
    fWrite = saveLoc.write
    fWrite('Hash for file: ' + n + "\nCreated on " + date.isoformat() + "\n\n" )
    return s

def fileWrite(n, s):
    saveLoc = open(s, 'a+')
    prevData = saveLoc.read()
    fWrite = saveLoc.write
    fWrite(n + '\n')
    return s

