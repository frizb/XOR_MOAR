# XOR_MOAR
Simple Python Utilities Developed During CTF Events For XORing Data

##xorfiles.py  
```
root@kali:~/# python xorfiles.py -h
XOR Binary Files: 0.1 Updated: August 28, 2018
usage: xorfiles.py [-h] [-basefile file] [-xorfile file] [-output file]

Very simple tool that XORs two binary files together

optional arguments:
  -h, --help      show this help message and exit
  -basefile file  Base binary file (default: base.bin)
  -xorfile file   XOR binary file (default: xor.bin)
  -output file    Output binary file (default: output.bin)


EXAMPLE:
root@kali:~/# python xorfiles.py -basefile base.bin -xorfile xorkey.bin
XOR Binary Files: 0.1 Updated: August 28, 2018
Wrote xor binary output to file: output.bin

```

##base64tobin.py
```
root@kali:~/# python base64tobin.py -h
Base64 to Binary: 0.1 Updated: August 28, 2018
usage: base64tobin.py [-h] [-input file] [-output file]

Very simply converter for BASE64 files to a Binary format

optional arguments:
  -h, --help    show this help message and exit
  -input file   Input BASE64 file (default: base64.txt)
  -output file  Output binary file (default: binary.bin)

EXAMPLE:
root@kali:~/# python base64tobin.py -input base64.txt -output ouput.bin
Base64 to Binary: 0.1 Updated: August 28, 2018
Wrote binary to file: output.bin
```

##XORBruteForce.py
Very raw XOR Brute Forcing Script.  Work in progres....
