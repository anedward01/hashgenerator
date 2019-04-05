# Hash Generator - Creates a hash using multiple methods
# Copyright (C) 2019  Anguianoewi

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import os

def cls():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')