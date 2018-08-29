import argparse

def xor(data, key):
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key])))

print('\033[0;32m'+"XOR Binary Files: " + '0.1' + " Updated: " + 'August 28, 2018' +'\033[0;39m')
parser = argparse.ArgumentParser(description='\033[0;31m'+'Very simple tool that XORs two binary files together'+'\033[0;39m')
parser.add_argument("-basefile", metavar='file', type=str, default="base.bin", help='Base binary file (default: %(default)s)')
parser.add_argument("-xorfile", metavar='file', type=str, default="xor.bin", help='XOR binary file (default: %(default)s)')
parser.add_argument("-output", metavar='file', type=str, default="output.bin", help='Output binary file (default: %(default)s)')
args = parser.parse_args()

with open(args.basefile, "r") as filein:
    basefile_content = filein.read()

with open(args.xorfile, "r") as filein:
    xorfile_content = filein.read()

with open(args.output,"w") as fileout:
	fileout.write(xor(basefile_content,xorfile_content))

print("Wrote xor binary output to file: " +args.output)