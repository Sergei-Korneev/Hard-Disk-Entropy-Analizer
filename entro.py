import string, getopt, sys, os, array, math, re, collections
from datetime import datetime






if (sys.version_info.major != 3 and sys.version_info.minor != 8):
    print("This script is tested on Python 3.8!")
    print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))
    sys.exit(1)

def entropy(data):
        e = 0

        counter = collections.Counter(data)
        l = len(data)
        for count in counter.values():
            # count is always > 0
            p_x = count / l
            e += - p_x * math.log2(p_x)

        return e
        
        
        
f = open("\\\\.\\physicaldrive0", 'rb')
sector=177301604
#sector=0  #first sector
f.seek(sector * 512)


block=100000   #sectors that will be read in one step
read = f.read(block)
while read:
 f.seek(sector * 512)
 read = f.read(block*512) 
 s=entropy(read)
 if s>7.95:
   print("Sector: {} | {}Mb | Entropy: {} <---".format(str(sector)+"-"+str(sector+block/512),str((sector*512)/1024/1024) ,  str(s)) )
   #break
 else:
   print("Sector: {} | {}Mb | Entropy: {} ".format(str(sector)+"-"+str(sector+block/512),str((sector*512)/1024/1024) ,  str(s)))
 sector+=block
f.close()