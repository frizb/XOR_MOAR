import base64
def xor(data, key):
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key])))

#cypher = bytearray(b'\x0a\xa9\x76\x5d\x08\xd7\xad\x10\xff\xfd\xe5\xc1\x82\x30\xa8')`
#\x0a\xa9\x76\x5d\x08\xd7 \xad\x10\xff\xfd\xe5\xc1\x82\x30\xa8
#\xc3\xd6\xcd\xc9\xc9\xa9\xbc\xb4\xb6\xb7\xa9\xdd\xd4\xcc\xc3
#print repr(base64.b64decode("MXCGG'89?<'NN@D"))

#print repr(xor(bytearray(b'\x0a\xa9\x76\x5d\x08\xd7\xad\x10\xff\xfd\xe5\xc1\x82\x30\xa8'),base64.b64decode("w9bNycmpvLS2t6nd1MzD")))

for x in range(255):
    bytesarray= [x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x]
    print hex(x) + " - " + xor("MXCGG'89?<'NN@D",bytesarray)

    #M

