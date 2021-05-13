#Python script for data entropy analysis
#Sergei Korneev

import string, getopt, sys, os, array, math, re, collections
from sys import stdout

import matplotlib.pyplot as plt
import numpy


    
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
        


hdd="\\\\.\\physicaldrive0"
#hdd="C:\\Users\\sergei\\Desktop\\noname"
block=512   #sectors that will be read in one step
#sector=177301604
sector=0  #first sector
endsector=177916081
start=sector

hl, = plt.plot([], [])
plt.title('Entropy Graph') 
plt.xlabel('x - Sectors') 
plt.ylabel('y - Entropy') 
def update_line(hl, xd,yd):
    hl.set_xdata(numpy.append(hl.get_xdata(), xd))
    hl.set_ydata(numpy.append(hl.get_ydata(), yd))
    plt.draw()        

        
f = open(hdd, 'rb')
f.seek(sector * 512)

read = f.read(block)
while read:
 if sector>endsector:
  break
 f.seek(sector * 512)
 read = f.read(block*512) 
 s=entropy(read)
 update_line(hl,round(sector)-start,s)
 
 if s>7.95:
   print("Sector: {} | {}Mb | Entropy: {} <---".format(str(sector)+"-"+str(round(sector+block/512)),str(round((sector*512)/1024/1024)) ,  str(round(s,3))))
   #break
 else:
   print("Sector: {} | {}Mb | Entropy: {} ".format(str(sector)+"-"+str(round(sector+block/512)),str(round((sector*512)/1024/1024)) ,  str(round(s,3))), end="\r")
   #print("Progress {:2.1%}".format(x / 10), end="\r")
 sector+=block

f.close()
plt.axis([0, endsector-start, 0, 10])
plt.show()
