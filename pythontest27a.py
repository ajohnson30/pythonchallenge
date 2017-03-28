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
print pal

myFile = open("zigzag.chain.txt","w")
for i in [0,2,6,7,16]:
 pal = im.getpalette()[0::3]
 j = i
 s = ""
 if pal[j] > i:
  s = s + myHex(j) + " "
 while pal[j] > i:
  s = s + myHex(pal[j]) + " "
  t=j
  j = pal[j]
  pal[t]=0
  if pal[j]<=i:
   pal[j]=0
   print "chain",i,"ended with",pal[j],"with",len(s)/3,"entries"
   print s
   myFile.write(s+chr(13))
 print

 im2 = Image.new("P",(16,16))
 for j in range(16):
  s=""
  for k in range(16):
   s = s + myHex(pal[j*16+k]) + " "
   if pal[j*16+k]==0:
    im2.putpixel((k,j),255)

  print s

 print
 im2.save("zigzag3-"+str(i)+".gif")

myFile.close()
