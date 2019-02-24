#imports modules from system and subdirectories
import sys
import os
import os.path
import subFiles.cls
import hashFiles.md5
import hashFiles.sha1
import hashFiles.sha224
import hashFiles.sha256
import hashFiles.sha384
import hashFiles.sha512
import hashFiles.sha3_224
import hashFiles.sha3_256
import hashFiles.sha3_384
import hashFiles.sha3_512
import hashFiles.shake128
import hashFiles.shake256
import hashFiles.blake2b
import hashFiles.blake2s

#Defines arguments used later in the code.
_cls____  = subFiles.cls.cls
_m5s____  = hashFiles.md5.s
_s1_1s    = hashFiles.sha1.s
_s1_224s  = hashFiles.sha224.s
_s1_256s  = hashFiles.sha256.s
_s1_384s  = hashFiles.sha384.s
_s1_512s  = hashFiles.sha512.s
_s3_224s  = hashFiles.sha3_224.s
_s3_256s  = hashFiles.sha3_256.s
_s3_384s  = hashFiles.sha3_384.s
_s3_512s  = hashFiles.sha3_512.s
_sh_128s  = hashFiles.shake128.s
_sh_256s  = hashFiles.shake256.s
_blake2bs = hashFiles.blake2b.s
_blake2ss = hashFiles.blake2s.s

def s(n):
    for i in range(999999):
        _cls____()
        print('String: "' + n + '"')
        hashType = input('Hash method: ')
        hType = hashType.lower().replace(' ','').strip()
        print('')
        isFin = False

        if 'md5' in hType:
            _m5s____(n)
            isFin = True

        if 'sha1' in hType:
            _s1_1s(n)
            isFin = True

        if 'sha224' in hType:
            _s1_224s(n)
            isFin = True

        if 'sha256' in hType:
            _s1_256s(n)
            isFin = True
        
        if 'sha384' in hType:
            _s1_384s(n)
            isFin = True

        if 'sha512' in hType:
            _s1_512s(n)
            isFin = True

        if 'sha3224' in hType:
            _s3_224s(n)
            isFin = True

        if 'sha3256' in hType:
            _s3_256s(n)
            isFin = True

        if 'sha3384' in hType:
            _s3_384s(n)
            isFin = True

        if 'sha3512' in hType:
            _s3_512s(n)
            isFin = True

        if 'shake128' in hType:
            _sh_128s(n)
            isFin = True

        if 'shake256' in hType:
            _sh_256s(n)
            isFin = True

        if 'blake2b' in hType:
            _blake2bs(n)
            isFin = True
            
        if 'blake2s' in hType:
            _blake2ss(n)
            isFin = True

        if isFin == True:
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n
        else:
            continue