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
_m5f____  = hashFiles.md5.f
_s1_1f    = hashFiles.sha1.f
_s1_224f  = hashFiles.sha224.f
_s1_256f  = hashFiles.sha256.f
_s1_384f  = hashFiles.sha384.f
_s1_512f  = hashFiles.sha512.f
_s3_224f  = hashFiles.sha3_224.f
_s3_256f  = hashFiles.sha3_256.f
_s3_384f  = hashFiles.sha3_384.f
_s3_512f  = hashFiles.sha3_512.f
_sh_128f  = hashFiles.shake128.f
_sh_256f  = hashFiles.shake256.f
_blake2bf = hashFiles.blake2b.f
_blake2sf = hashFiles.blake2s.f
def f(n):
    for i in range(999999):
        _cls____()
        print('File Path: "' + n + '"')
        hashType = input('Hash method: ')
        hType = hashType.lower().replace(' ','').strip()
        print('')
        isFin = False

        if 'md5' in hType:
            print('MD5:       ' + _m5f____(n))
            isFin = True

        if 'sha1' in hType:
            print('SHA 1:     ' + _s1_1f(n))
            isFin = True

        if 'sha224' in hType:
            print('SHA 224:   ' + _s1_224f(n))
            isFin = True

        if 'sha256' in hType:
            print('SHA 256:   ' + _s1_256f(n))
            isFin = True
        
        if 'sha384' in hType:
            print('SHA 384:   ' + _s1_384f(n))
            isFin = True

        if 'sha512' in hType:
            print('SHA 512:   ' + _s1_512f(n))
            isFin = True

        if 'sha3224' in hType:
            print('SHA3 224:  ' + _s3_224f(n))
            isFin = True

        if 'sha3256' in hType:
            print('SHA3 256:  ' + _s3_256f(n))
            isFin = True

        if 'sha3384' in hType:
            print('SHA3 384:  ' + _s3_384f(n))
            isFin = True

        if 'sha3512' in hType:
            print('SHA3 512:  ' + _s3_512f(n))
            isFin = True

        if 'shake128' in hType:
            print('SHAKE 128: ' + _sh_128f(n))
            isFin = True

        if 'shake256' in hType:
            print('SHAKE 256: ' + _sh_256f(n))
            isFin = True

        if 'blake2b' in hType:
            print('BLAKE2B:   ' + _blake2bf(n))
            isFin = True

        if 'blake2s' in hType:
            print('BLAKE2S:   ' + _blake2sf(n))
            isFin = True

        if isFin == True:
            _nul = input('Press Enter to continue...')
            _cls____()
            break
            return n
        else:
            continue
