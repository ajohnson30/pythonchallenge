import Image
import ImagePalette
import operator
import bz2
import keyword
import sys

def myHex(h):
 ii = hex(h)[2:]
 if len(ii) < 2:
  ii = '0' + ii
 return ii

im = Image.open("zigzag.gif")
print "image size is", im.size


pal = im.getpalette()[0::3]
d = im.getdata()
g = []


for i in range(len(d)-1):
 if d[i+1]<>pal[d[i]]:
  g.append(d[i+1])

print str(g[:10])
longString = ""

for i in range(len(g)):
 longString = longString + chr(g[i])

longString = bz2.decompress(longString)


#print longString


kwds = longString.split()

print keyword.iskeyword("def")

for w in kwds:
 if keyword.iskeyword(w) == False:
  print w
