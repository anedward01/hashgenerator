#imports modules from system and subdirectories
import sys
import os
import os.path
import subFiles.cls as  cls_
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
_md5s___  = md5.s
_s1_1s__  = sha1.s
_s1_224s  = sha224.s
_s1_256s  = sha256.s
_s1_384s  = sha384.s
_s1_512s  = sha512.s
_s3_224s  = sha3_224.s
_s3_256s  = sha3_256.s
_s3_384s  = sha3_384.s
_s3_512s  = sha3_512.s
_sh_128s  = shake128.s
_sh_256s  = shake256.s
_blake2bs = blake2b.s
_blake2ss = blake2s.s
_sh_128cs = shake128c.s
_sh_256cs = shake256c.s

def s(n):
    for i in range(999999):
        _cls____()
        print('String: "' + n + '"')
        hashType = input('Hash method: ')
        hType = hashType.lower().replace(' ','').strip()
        print('')
        isFin = False

        if 'md5' in hType:
            print('MD5:            ' + _md5s___(n))
            isFin = True

        if 'sha1' in hType:
            print('SHA 1:          ' + _s1_1s__(n))
            isFin = True

        if 'sha224' in hType:
            print('SHA 224:        ' + _s1_224s(n))
            isFin = True

        if 'sha256' in hType:
            print('SHA 256:        ' + _s1_256s(n))
            isFin = True
        
        if 'sha384' in hType:
            print('SHA 384:        ' + _s1_384s(n))
            isFin = True

        if 'sha512' in hType:
            print('SHA 512:        ' + _s1_512s(n))
            isFin = True

        if 'sha3224' in hType:
            print('SHA3 224:       ' + _s3_224s(n))
            isFin = True

        if 'sha3256' in hType:
            print('SHA3 256:       ' + _s3_256s(n))
            isFin = True

        if 'sha3384' in hType:
            print('SHA3 384:       ' + _s3_384s(n))
            isFin = True

        if 'sha3512' in hType:
            print('SHA3 512:       ' + _s3_512s(n))
            isFin = True

        if 'shake128c' in hType:
            print('SHAKE 128 FULL: ' + _sh_128cs(n))
            isFin = True

        if 'shake128' in hType:
            print('SHAKE 128 (64): ' + _sh_128s(n))
            isFin = True

        if 'shake256c' in hType:
            print('SHAKE 256 FULL: ' + _sh_256cs(n))
            isFin = True
        
        if 'shake256' in hType:
            print('SHAKE 256 (64): ' + _sh_256s(n))
            isFin = True

        if 'blake2b' in hType:
            print('BLAKE2B:        ' + _blake2bs(n))
            isFin = True

        if 'blake2s' in hType:
            print('BLAKE2S:        ' + _blake2ss(n))
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