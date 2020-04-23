import string, getopt, sys, os, array, math, re, collections
from sys import stdout
hdd="\\\\.\\physicaldrive0"
#hdd="C:\\Users\\sergei\\Desktop\\noname"
block=96   #sectors that will be read in one step
#sector=177301604
sector=0  #first sector


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
        
        
        
f = open(hdd, 'rb')

f.seek(sector * 512)



read = f.read(block)
while read:
 
 f.seek(sector * 512)
 read = f.read(block*512) 
 s=entropy(read)
 if s>7.95:
   print("Sector: {} | {}Mb | Entropy: {} <---".format(str(sector)+"-"+str(sector+block/512),str(round((sector*512)/1024/1024)) ,  str(round(s,3))))
   #break
 else:
   print("Sector: {} | {}Mb | Entropy: {} ".format(str(sector)+"-"+str(sector+block/512),str(round((sector*512)/1024/1024)) ,  str(round(s,3))), end="\r")
   #print("Progress {:2.1%}".format(x / 10), end="\r")
 sector+=block
 sys.stdout.flush()
f.close()
