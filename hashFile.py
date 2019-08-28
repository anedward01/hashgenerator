# Hash Generator - Creates a hash using multiple methods
# Copyright (C) 2019  Anguianoewi

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import sys
import os
import os.path
import subFiles.cls as  cls_
import subFiles.exportToFile as expFile
import hashFiles.md5 as md5
import hashFiles.sha1 as sha1
import hashFiles.sha224 as sha224
import hashFiles.sha256 as sha256
import hashFiles.sha384 as sha384
import hashFiles.sha512 as sha512
import hashFiles.sha3_224 as sha3_224
import hashFiles.sha3_256 as sha3_256
import hashFiles.sha3_384 as sha3_384
import hashFiles.sha3_512 as sha3_512
import hashFiles.shake128 as shake128
import hashFiles.shake128_Complete as shake128c
import hashFiles.shake256 as shake256
import hashFiles.shake256_Complete as shake256c
import hashFiles.blake2b as blake2b
import hashFiles.blake2s as blake2s

#Defines arguments used later in the code.
_cls____  = cls_.cls
_md5f___  = md5.f
_s1_1f__  = sha1.f
_s1_224f  = sha224.f
_s1_256f  = sha256.f
_s1_384f  = sha384.f
_s1_512f  = sha512.f
_s3_224f  = sha3_224.f
_s3_256f  = sha3_256.f
_s3_384f  = sha3_384.f
_s3_512f  = sha3_512.f
_sh_128f  = shake128.f
_sh_256f  = shake256.f
_blake2bf = blake2b.f
_blake2sf = blake2s.f
_sh_128cf = shake128c.f
_sh_256cf = shake256c.f
_writeH = expFile.fileWrite
_writeT = expFile.titleWrite

""" This function is natively called by mainProgram.py to finish acquiring
information to hash file"""
def f(n):
    for i in range(999999):
        _cls____()
        print('File Path: "' + n + '"')
        print('Save to file? [Y]es | [N]o')
        saveFile = input()
        sFile = saveFile.lower().replace (' ','').strip()

        if sFile == 'yes' or sFile == 'y':
            saveToFile = 1
            expMod = 1
            while os.path.exists('Saved Hash File ' + str(expMod) + '.txt'):
                expMod += 1
            saveLocation = ('Saved Hash File ' + str(expMod) + '.txt')
            print('Enter file name or leave empty for default')
            print('Saved Hash File ' + str(expMod))
            fileName = input()
            if fileName == '' or fileName == None:
                _writeT(n, saveLocation)
            else:
                saveLocation = fileName
                _writeT(n, saveLocation)
            print('Hash file "' + saveLocation + '" created in source folder.')
        

        hashType = input('Hash method: ')
        hType = hashType.lower().replace(' ','').strip()
        print('')
        isFin = False

        if 'shake128c' in hType:
            hb128 = input('Enter shake128 byte size: ')

        if 'shake256c' in hType:
            hb256 = input('Enter shake256 byte size: ')
            
        if 'md5' in hType:
            __md5 = ('MD5:            ' + _md5f___(n))
            print(__md5)
            if saveToFile == 1:
                _writeH(__md5, saveLocation)
            isFin = True

        if 'sha1' in hType:
            __sha1 = ('SHA 1:          ' + _s1_1f__(n))
            print(__sha1)
            if saveToFile == 1:
                _writeH(__sha1, saveLocation)
            isFin = True

        if 'sha224' in hType:
            __sha224 = ('SHA 224:        ' + _s1_224f(n))
            print(__sha224)
            if saveToFile == 1:
                _writeH(__sha224, saveLocation)
            isFin = True

        if 'sha256' in hType:
            __sha256 = ('SHA 256:        ' + _s1_256f(n))
            print(__sha256)
            if saveToFile == 1:
                _writeH(__sha256, saveLocation)
            isFin = True
        
        if 'sha384' in hType:
            __sha384 = ('SHA 384:        ' + _s1_384f(n))
            print(__sha384)
            if saveToFile == 1:
                _writeH(__sha384, saveLocation)
            isFin = True

        if 'sha512' in hType:
            __sha512 = ('SHA 512:        ' + _s1_512f(n))
            print(__sha512)
            if saveToFile == 1:
                _writeH(__sha512, saveLocation)
            isFin = True

        if 'sha3224' in hType:
            __sha3_224 = ('SHA3 224:       ' + _s3_224f(n))
            print(__sha3_224)
            if saveToFile == 1:
                _writeH(__sha3_224, saveLocation)
            isFin = True

        if 'sha3256' in hType:
            __sha3_256 = ('SHA3 256:       ' + _s3_256f(n))
            print(__sha3_256)
            if saveToFile == 1:
                _writeH(__sha3_256, saveLocation)
            isFin = True

        if 'sha3384' in hType:
            __sha3_384 = ('SHA3 384:       ' + _s3_384f(n))
            print(__sha3_384)
            if saveToFile == 1:
                _writeH(__sha3_384, saveLocation)
            isFin = True

        if 'sha3512' in hType:
            __sha3_512 = ('SHA3 512:       ' + _s3_512f(n))
            print(__sha3_512)
            if saveToFile == 1:
                _writeH(__sha3_512, saveLocation)
            isFin = True

        if 'shake128' in hType:
            __sh128 = ('SHAKE 128 (64): ' + _sh_128f(n))
            print(__sh128)
            if saveToFile == 1:
                _writeH(__sh128, saveLocation)
            isFin = True

        if 'shake128c' in hType:
            __sh128c = ('SHAKE 128 FULL: ' + _sh_128cf(n, hb128))
            print(__sh128c)
            if saveToFile == 1:
                _writeH(__sh128c, saveLocation)
            isFin = True

        if 'shake256' in hType:
            __sh256 = ('SHAKE 256 (64): ' + _sh_256f(n))
            print(__sh256)
            if saveToFile == 1:
                _writeH(__sh256, saveLocation)
            isFin = True

        if 'shake256c'  in hType:
            __sh256c = ('SHAKE 256 FULL: ' + _sh_256cf(n, hb128))
            print(__sh256c)
            if saveToFile == 1:
                _writeH(__sh256c, saveLocation)
            isFin = True

        if 'blake2b' in hType:
            __bla2b = ('BLAKE2B:        ' + _blake2bf(n))
            print(__bla2b)
            if saveToFile == 1:
                _writeH(__bla2b, saveLocation)
            isFin = True

        if 'blake2s' in hType:
            __bla2s = ('BLAKE2S:        ' + _blake2sf(n))
            print(__bla2s)
            if saveToFile == 1:
                _writeH(__bla2s, saveLocation)
            isFin = True
        
        if hType == 'e' or hType =='exit':
            sys.exit(0)

        if isFin == True:   
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n

        else:
            continue