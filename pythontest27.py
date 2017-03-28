import Image
import ImagePalette
import operator

def myHex(h):
 ii = hex(h)[2:]
 if len(ii) < 2:
  ii = '0' + ii
 return ii

im = Image.open("zigzag.gif")
im2 = Image.new("P",(320,270))

print "image size is", im.size

im2.putdata(im.getdata())

pal = im.getpalette()
pal2 = []
for i in range(768):
 pal2 = pal2 + [0]

for i in [0,2,6,7,16]:
 k = 0
 for j in range(256):
  pal2[j*3] = 0
  pal2[j*3+1] = 0
  pal2[j*3+2] = 0

 j = i
 if pal[j*3] > i:
  pal2[i*3] = 255
  pal2[i*3+1] = 255
  pal2[i*3+2] = 255
 while pal[j*3] > i:
  pal2[j*3] = 255
  pal2[j*3+1] = 255
  pal2[j*3+2] = 255
  j = pal[j*3]
  k = k + 1
 im2.putpalette(pal2)
 fname = "zigzag2-" + str(i) + ".gif"
 print fname,"changed",k,"entries"
 im2.save(fname)
