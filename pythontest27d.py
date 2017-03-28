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

h = "   "
r = ""
s = ""
t = ""
for i in range(16):
 r = r + myHex(i) + "|"
 s = s + myHex(i) + "|"
 t = t + myHex(i) + "|"

 h = h + myHex(i) + " "
 for j in range(16):
  r = r + myHex(pal[i*16+j])  + " "
  s = s + myHex(pal[pal[i*16+j]])  + " "
  t = t + myHex(pal[pal[pal[i*16+j]]]) + " "
 r = r + chr(13) + chr(10)
 s = s + chr(13) + chr(10)
 t = t + chr(13) + chr(10)

myFile = open("zigzag.palzigs.txt","w")
myFile.write(h + chr(13) + chr(10))
myFile.write(r + chr(13) + chr(10))
myFile.write(h + chr(13) + chr(10))
myFile.write(s + chr(13) + chr(10))
myFile.write(h + chr(13) + chr(10))
myFile.write(t + chr(13) + chr(10))
myFile.close()
