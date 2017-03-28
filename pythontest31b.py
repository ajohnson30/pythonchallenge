import Image 
import ImagePalette

def mkpalette():
 global palette
 palette = [0,0,0]

 for i in range(0,255):
  palette.extend((0, 0, i))        
 return palette

def fractalpoint(x,y,n):
 z = complex(x,y)
 o = complex(0,0)
 for iters in range(n):
  if abs(o) > 2.0:
   break
  o = o**2 + z
 return iters-1

mySize = [640,480]
xx = 0.34
yy = 0.57
dx = 0.036
dy = 0.027
n = 129

im = Image.new('P',mySize)
im2 = Image.open('mandelbrot.gif',"r")
im.putpalette(im2.getpalette())


i = 0
j = 0

for x in range(mySize[0]):
 for y in range(mySize[1]):

  xp = xx + dx*x/mySize[0]
  yp = yy + dy*y/mySize[1]

  dotcolor = fractalpoint(xp,yp,n)
  im.putpixel((x,mySize[1]-y-1),dotcolor)

im.save("myfractal.gif")

longString1 = im.getdata()
longString2 = im2.getdata()

j=0
s=''
for i in range(len(longString1)):
 if longString1[i] <> longString2[i]:
  s = s + longString2[i]
  j = j + 1
  if j%73 == 0:
   print s
   s = ''
 if j > 1700:
  break

print
print j

#1679 is 73 x 23

