# Hash Generator - Creates a hash using multiple methods
# Copyright (C) 2019  Anguianoewi

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import sys
import os
import subFiles.cls
import subFiles.title

#Defines arguments used in the code
_cls____ = subFiles.cls.cls
_version = subFiles.title.version

#Endless loop until exit
def h():
    _cls____()
    print('Hash Converter Help.')
    while True:
        print('[H]ash Methods | [C]redits | [E]xit')
        helpOption = input()
        hOpt = helpOption.lower().strip().replace(' ','')
        if hOpt == 'hashmethods' or hOpt == 'h' or hOpt == 'hash' or hOpt == 'hashmethod':
            print('''The following hash methods are available:
MD5     | SHA 384   | SHA3 384
SHA 1   | SHA 512   | SHA3 512
SHA 224 | SHA3 224  | SHAKE 128 (64 bit)
SHA 256 | SHA3 256  | SHAKE 256 (64 bit)
BLAKE2B | BLAKE2S   |''')
            print('')
            cont = input('Press Enter to continue')
            _cls____()
            True
        elif hOpt == 'c' or hOpt == 'credits' or hOpt == 'credit':
            print('''Hash Generator Version ' ''' + _version())
            print('''
For suggestions, visit https://github.com/anguianoewi/hashgenerator
This code is free to use. Only requirement is to give credit where due
Author:              Anguianoewi
Created on:          Python 3.7.2 with hashlib module.
Executable:          Pyinstaller used to create file
Modules:             Developed by Anguianoewi using functions
Special Recognition: StackOverflow and everyone involved in Python forums
                     Luke Sudtelgte for motivating me into coding. Thanks pal
                     Al Sweigart for teaching me to automate the boring stuff

This project started in March 2018, and entered into the public domain in February
2019 after I figured out how to take 600 lines of code from one file and break it
down into smaller and manageable files.''')
            cont = input('Press Enter to continue')
            _cls____()
            True
        elif hOpt == 'e' or hOpt == 'exit':
            _cls____()
            return hOpt
        else:
            False