# Hash Generator - Creates a hash using multiple methods
# Copyright (C) 2019  Anguianoewi

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import os

def version():
    vers = '3.0.3'
    return vers

def title():
    if os.name == 'nt':
        _ = os.system('title Hash Generator V. ' + version())
    else:
        x = 5