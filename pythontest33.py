import Image
import math

def myHex(h):
 ii = hex(h)[2:]
 if len(ii) < 2:
  ii = '0' + ii
 return ii

def maxpixels(i):
 n=0
 for j in range(len(i)):
  if i[j]>0:
   n=j
 return n
  

im = Image.open("beer2.png","r")

hist = im.histogram()

longstring=im.getdata()
print longstring[0]

k=0

for i in range(66):
 longstring2=""
 p = maxpixels(hist)
 hist[p]=0
 for j in range(len(longstring)):
  if longstring[j]<p:
   longstring2=longstring2+chr(longstring[j])
 print i,len(longstring2),chr(13),

 if math.sqrt(len(longstring2)) == int(math.sqrt(len(longstring2))) and len(longstring2)>0:
  print "Possible picture with size",math.sqrt(len(longstring2)),"after",i,"iterations",p
  xx=int(math.sqrt(len(longstring2)))
  yy=xx
  im2=Image.new("L",(xx,yy))
  m=0
  for n in range(len(longstring2)):
   if ord(longstring2[n])>m:
    m = ord(longstring2[n])
  for y in range(yy):
   for x in range(xx):
    if ord(longstring2[y*xx+x]) == m:
     im2.putpixel((x,y),255)
  if k < 10:
   fname = "beer2-0" + str(k) + ".png"
  else:
   fname = "beer2-" + str(k) + ".png"
  im2.save(fname)
  k=k+1
