import urllib
import operator
import bz2
from math import sqrt
import Image

def factorize(n):
    def isPrime(n):
        return not [x for x in xrange(2,int(sqrt(n))+1)
                    if n%x == 0]
    primes = []
    candidates = xrange(2,n+1)
    candidate = 2
    while not primes and candidate in candidates:
        if n%candidate == 0 and isPrime(candidate):
            primes = primes + [candidate] + factorize(n/candidate)
        candidate += 1            
    return primes

def myHex(h):
 ii = hex(h)[2:]
 if len(ii) < 2:
  ii = '0' + ii
 return ii


nexturl = 'http://repeat:switch@www.pythonchallenge.com/pc/ring/yankeedoodle.csv'

myFile = urllib.urlopen(nexturl)
headers = myFile.info() 
#print headers
LongString = myFile.read()
#print LongString
print len(LongString)
myFile.close()

#myFile = open("yankeedoodle.csv","w")
#myFile.write(LongString)
#myFile.close()

s = LongString.replace('\n','').replace(' ','').split(',')

print len(s)
print factorize(len(s))

im = Image.new("RGB",(53,139))

for y in range(139):
 for x in range(53):
  p = int(float(s[x+(y*53)])*256)
  im.putpixel((x,y),(p,p,p))
im.save("yankeedoodle.bmp")

