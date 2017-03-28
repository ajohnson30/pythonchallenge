import urllib
import operator
import bz2

def myHex(h):
 ii = hex(h)[2:]
 if len(ii) < 2:
  ii = '0' + ii
 return ii


nexturl = 'http://repeat:switch@www.pythonchallenge.com/pc/ring/guido.html'

myFile = urllib.urlopen(nexturl)
headers = myFile.info() 
#print headers
LongString = myFile.read()
#print LongString
#print len(LongString)
myFile.close()

myLines = LongString.splitlines()

myFile = open("pythontest29.hex.txt","w")
for i in range(len(LongString)):
 if ord(LongString[i]) == 10:
  myFile.write(chr(13) + chr(10))
 else:
  myFile.write(myHex(ord(LongString[i])) + " ")
myFile.close()

s=""
t=""
for i in range(len(myLines)):
 if i > 11:
  j = len(myLines[i])
  t = t + str(j) + ", "
  s=s+chr(j)
 print t
print s
t = bz2.decompress(s)
print t
