# Hash Generator - Creates a hash using multiple methods
# Copyright (C) 2019  Anguianoewi

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import os
import sys
import os.path
import datetime

def titleWrite(n, s):
    date = datetime.datetime.now()
    if '.txt' in s:
        saveLoc = open(s, 'w+')
        fWrite = saveLoc.write
        fWrite('Hash for file: ' + n + "\nCreated on " + date.isoformat() + "\n\n" )
        return s
    else:
        saveLoc = open(s + '.txt', 'w+')
        fWrite = saveLoc.write
        fWrite('Hash for file: ' + n + "\nCreated on " + date.isoformat() + "\n\n" )
        return s

def fileWrite(n, s):
    if '.txt' in s:
        saveLoc = open(s, 'a+')
        prevData = saveLoc.read()
        fWrite = saveLoc.write
        fWrite(n + '\n')
        return s
    else:
        saveLoc = open(s + '.txt', 'a+')
        prevData = saveLoc.read()
        fWrite = saveLoc.write
        fWrite(n + '\n')
        return s

