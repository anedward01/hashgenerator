# Hash Generator - Creates a hash using multiple methods
# Copyright (C) 2019  Anguianoewi

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import hashlib
import sys
import os
import os.path

#This is non-verbose. The program will run accordingly and release a message.
BLOCKSIZE=65536


def f(n):
    _h = hashlib.shake_256()
    with open(n, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            _h.update(buf)
            H = _h.hexdigest(64)
            buf = afile.read(BLOCKSIZE)
        return H

def s(n):
    _h = hashlib.shake_256()
    buf = n.encode()
    _h.update(buf)
    H = _h.hexdigest(64)
    return H