# Hash Generator - Creates a hash using multiple methods
# Copyright (C) 2019  Anguianoewi

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>

import sys
import os
import hashFile
import hashString
import subFiles.cls
import subFiles.title
import subFiles.helpMain
import subFiles.pathCheck

_cls = subFiles.cls.cls
_title = subFiles.title.title
_help = subFiles.helpMain.h
_vers = subFiles.title.version
_path = subFiles.pathCheck.checkPath

_cls()
_title()

print('Hash Generator - Creates checksums using multiple methods\n'
'Copyright (C) 2019  Anguianoewi\n\n'
'You should have received a copy of the GNU General Public License\n'
'along with this program.  If not, see <http://www.gnu.org/licenses/>\n')
input('Press Enter to continue')
_cls()

while True:
    print('Hash Generator Version ' + _vers())
    fileType = input('[S]tring | [F]ile | [H]elp | [E]xit: ')
    fType = fileType.lower().replace(' ','').strip()

    if fType == 'file' or fType == 'f':
        fileCheckVar = False
        while fileCheckVar is False:
            filePath = input('File Path: ')
            fP = filePath.lower().strip().replace(' ','')
            formalFile = _path(filePath)
            if fP == "exit" or fP == "e" or fP =='quit':
                sys.exit(0)
            elif formalFile == None:
                print('File location does not exist!')
            else:
                hashFile.f(formalFile)
                fileCheckVar = True

    elif fType == 'string' or fType == 's':
        string = input('String: ')

        stringStrip = input('Strip white space? ([Y]es | [N]o): ')
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