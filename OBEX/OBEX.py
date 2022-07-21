import sys
from os.path import basename
from lightblue.obex import OBEXClient

if len(sys.argv) < 4:
    print(sys.argv[0] + " : <btaddr> <channel> <file>")
    sys.exit(0)

btaddr = sys.argv[1]
channel = int(sys.argv[2])
mfile = sys.argv[3]

print("sending %s to %s on channel %d"%(mfile ,btaddr ,channel))

obex = OBEXClient(btaddr ,channel)
obex.connect()
obex.put({'name': basename(mfile)} ,open(mfile ,"rb"))
obex.disconnect()