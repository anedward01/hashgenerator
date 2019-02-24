# hashgenerator
A simple Python program that gives 14 different hashing options for files and text.

# Files
1) Files must be located with the drive path. For example: 
"C:\Users\anguianoewi\Downloads\hashgenerator\hashSource\mainProgram.py"
2) The file is converted into a hash after selecting hash method

# Text
1) Text is typed into the program.
2) The user then has to option to remove accidental trailing space.
3) The text is converted into a hash after selecting hash method.

# Hash Methods

There are twelve hash methods available.

One hash method or multiple can be used at once. simply type them in at once. 

The program does this by taking the input "md5 sha1 sha224sha 256 sha 384 sha 5 1 2 s  h  a  k  e  1  2  8    "

and removing spaces to make "md5sha1sha224sha256sha384sha512shake128"

then checking if the hash is in the text, such as 'md5' is in the string so MD5 hash will run


MD5     |  SHA 384   |  SHA3 384

SHA-1   |  SHA 512   |  SHA3 512

SHA 224 |  SHA3 224  |  SHAKE 128 (64-bit output)

SHA 256 |  SHA3 256  |  SHAKE 256 (64-bit output)

BLAKE2B | BLAKE2S

All fourteen work correctly and refresh every time its function is used.

# Hash Modules

The hash modules are inside the /hashFiles folder and are designed to
be truly modular and reuseable

Each hash module has two functions. The "f" 
function is called forth for file hashes. The 
"s" function is called forth for string hashes.

# OLD VERSION

Can be found at www.github.com/anguianoewi/hashgeneratorOld
