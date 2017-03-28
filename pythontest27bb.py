import Image
import ImagePalette
import operator

def myHex(h):
 ii = hex(h)[2:]
 if len(ii) < 2:
  ii = '0' + ii
 return ii

im = Image.open("zigzag.gif")
print "image size is", im.size


pal = im.getpalette()[0::3]

d = im.getdata()
e = []
g=[]
print d[0],d[1]
print pal.index(d[0]),pal[pal.index(d[0])],pal[pal[pal.index(d[0])]]
print len(d)
for i in range(len(d)-1):

 if operator.mod(i+1,100)==0:
  print i,chr(13),

 if d[i+1]<>pal[d[i]]:
  e.append(d[i+1])
 else:
  e.append(0)
print i

im.putdata(e)
im.save("zigzag2a.gif")

