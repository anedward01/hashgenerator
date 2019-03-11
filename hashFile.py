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

def f(n):
    __md5 = 'HASH NOT RUN'; __sha1 = 'HASH NOT RUN'; __sha224 = 'HASH NOT RUN'; __sha256 = 'HASH NOT RUN'; __sha384 = 'HASH NOT RUN'; __sha512 = 'HASH NOT RUN'
    __sha3_224 = 'HASH NOT RUN'; __sha3_256 = 'HASH NOT RUN'; __sha3_384 = 'HASH NOT RUN'; __sha3_512 = 'HASH NOT RUN'; __bla2s = 'HASH NOT RUN'
    __bla2b = 'HASH NOT RUN'; __sh128 = 'HASH NOT RUN'; __sh128c = 'HASH NOT RUN'; __sh256 = 'HASH NOT RUN'; __sh256c = 'HASH NOT RUN'
    for i in range(999999):
        _cls____()
        print('File Path: "' + n + '"')
        print('Would you like to save the results to a file?')
        saveFile = input()
        sFile = saveFile.lower().replace (' ','').strip()

        if sFile == 'yes' or sFile == 'y':
            saveToFile = 1

        hashType = input('Hash method: ')
        hType = hashType.lower().replace(' ','').strip()
        print('')
        isFin = False

        if 'md5' in hType:
            __md5 = ('MD5:            ' + _md5f___(n))
            print(__md5)
            isFin = True

        if 'sha1' in hType:
            __sha1 = ('SHA 1:          ' + _s1_1f__(n))
            print(__sha1)
            isFin = True

        if 'sha224' in hType:
            __sha224 = ('SHA 224:        ' + _s1_224f(n))
            print(__sha224)
            isFin = True

        if 'sha256' in hType:
            __sha256 = ('SHA 256:        ' + _s1_256f(n))
            print(__sha256)
            isFin = True
        
        if 'sha384' in hType:
            __sha384 = ('SHA 384:        ' + _s1_384f(n))
            print(__sha384)
            isFin = True

        if 'sha512' in hType:
            __sha512 = ('SHA 512:        ' + _s1_512f(n))
            print(__sha512)
            isFin = True

        if 'sha3224' in hType:
            __sha3_224 = ('SHA3 224:       ' + _s3_224f(n))
            print(__sha3_224)
            isFin = True

        if 'sha3256' in hType:
            __sha3_256 = ('SHA3 256:       ' + _s3_256f(n))
            print(__sha3_256)
            isFin = True

        if 'sha3384' in hType:
            __sha3_384 = ('SHA3 384:       ' + _s3_384f(n))
            print(__sha3_384)
            isFin = True

        if 'sha3512' in hType:
            __sha3_512 = ('SHA3 512:       ' + _s3_512f(n))
            print(__sha3_512)
            isFin = True

        if 'shake128' in hType:
            __sh128 = ('SHAKE 128 (64): ' + _sh_128f(n))
            print(__sh128)
            isFin = True

        if 'shake128c' in hType:
            __sh128c = ('SHAKE 128 FULL: ' + _sh_128cf(n))
            print(__sh128c)
            isFin = True

        if 'shake256' in hType:
            __sh256 = ('SHAKE 256 (64): ' + _sh_256f(n))
            print(__sh256)
            isFin = True

        if 'shake256c'  in hType:
            __sh256c = ('SHAKE 256 FULL: ' + _sh_256cf(n))
            print(__sh256c)
            isFin = True

        if 'blake2b' in hType:
            __bla2b = ('BLAKE2B:        ' + _blake2bf(n))
            print(__bla2b)
            isFin = True

        if 'blake2s' in hType:
            __bla2s = ('BLAKE2S:        ' + _blake2sf(n))
            print(__bla2s)
            isFin = True
        
        if hType == 'e' or hType =='exit':
            sys.exit(0)

        if isFin == True:
            if saveToFile == 1:
                hashWrite = open('HashFile.txt','w+')
                hWrite = hashWrite.write
                hWrite('File path: ' + n + '\n')
                hWrite(__md5 + '\n')
                hWrite(__sha1 + '\n')
                hWrite(__sha224 + '\n')
                hWrite(__sha256 + '\n')
                hWrite(__sha384 + '\n')
                hWrite(__sha512 + '\n')
                hWrite(__sha3_224 + '\n')
                hWrite(__sha3_256 + '\n')
                hWrite(__sha3_384 + '\n')
                hWrite(__sha3_512 + '\n')
                hWrite(__sh128 + '\n')
                hWrite(__sh128c + '\n')
                hWrite(__sh256 + '\n')
                hWrite(__sh256c + '\n')
                hWrite(__bla2b + '\n')
                hWrite(__bla2s + '\n')
                break
                return n
            else:    
                _nul = input('Press Enter to continue...')
                _cls____()
                break
                return n

        else:
            continue