import base64
import argparse


print('\033[0;32m'+"Base64 to Binary: " + '0.1' + " Updated: " + 'August 28, 2018' +'\033[0;39m')
parser = argparse.ArgumentParser(description='\033[0;31m'+'Very simple converter for BASE64 files to a Binary format'+'\033[0;39m')
parser.add_argument("-input", metavar='file', type=str, default="base64.txt", help='Input BASE64 file (default: %(default)s)')
parser.add_argument("-output", metavar='file', type=str, default="binary.bin", help='Output binary file (default: %(default)s)')
args = parser.parse_args()

with open(args.input, "r") as filein:
    base64_content = filein.read()

with open(args.output,"w") as fileout:
	fileout.write(base64.b64decode(base64_content))

print("Wrote binary to file: " +args.output)