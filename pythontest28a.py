import Image

im = Image.open("bell.png")

idata = im.getdata()

s=""

for x in range(len(idata)/2):

 j = idata[x*2+1][1] - idata[x*2][1]
 if j <> 42 and j <> -42:
  s = s + chr(abs(j))
print s

