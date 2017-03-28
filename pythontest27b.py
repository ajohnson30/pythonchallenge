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


pal = im.getpalette()

s = []
for i in [0,2,6,7,16]:
 ss = []
 pal = im.getpalette()[0::3]
 j = i
 if pal[j] > i:
  ss = ss + [j]
 while pal[j] > i:
  ss = ss + [pal[j]]
  t=j
  j = pal[j]
  pal[t]=0
  if pal[j]<=i:
   pal[j]=0
 s=s+ss+ss + [0]+[0]+[0]
for y in range(270):
 for x in range(318):
  i = im.getpixel((x,y))
  j = im.getpixel((x+1,y))
  k = im.getpixel((x+2,y))
  l=s.index(i)
  if l < len(s)-2:
   if (s[l+1]==j) and (s[l+2]==k):
    im.putpixel((x,y),0)
    im.putpixel((x+1,y),0)
    im.putpixel((x+2,y),0)
pal2 = [0] + [0] + [0]
for i in range(767):
 pal2 = pal2 + [255]
im.putpalette(pal2)
im.save("zigzag2.gif")

myFile = open("zigzag2.raw.txt","w")
for y in range(270):
 s = ""
 for x in range(320):
  i = im.getpixel((x,y))
  s = s + myHex(i) + " "
  if i > 32 and i < 123:
   print chr(i),
 myFile.write(s + chr(13) + chr(10))
myFile.close()
print
