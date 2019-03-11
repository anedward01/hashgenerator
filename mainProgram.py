import sys
import os
import os.path
import hashFile
import hashString
import subFiles.cls
import subFiles.title
import subFiles.helpMain

_cls = subFiles.cls.cls
_title = subFiles.title.title
_help = subFiles.helpMain.h
_vers = subFiles.title.version

_cls()
_title()

while True:
    print('Hash Generator Version ' + _vers())
    fileType = input('[S]tring | [F]ile | [H]elp | [E]xit: ')
    fType = fileType.lower().replace(' ','').strip()

    if fType == 'file' or fType == 'f':
        filePath = input('File Path: ')
        if os.path.exists(filePath):

            hashFile.f(filePath)
        else:
            print('File location does not exist!')

    elif fType == 'string' or fType == 's':
        string = input('String: ')

        stringStrip = input('Strip white space? ([Y]es | [N]o)')
        sStrip = stringStrip.lower().strip().replace(' ','')

        if sStrip == 'yes' or sStrip == 'y':
            sString = string.strip()
            hashString.s(sString)
            
        if sStrip == 'no' or sStrip == 'n':
            hashString.s(string)

    elif fType == 'h' or fType == 'help':
        _help()

    elif fType == 'e' or fType == 'exit':
        sys.exit(0)