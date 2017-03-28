import Image 
import ImagePalette

def mkpalette():
 global palette
 palette = [0,0,0]

 for i in range(0,255):
  palette.extend((0, 0, i))        
 return palette

def fractalpoint(x,y,n):
 xz=0.0
 yz=0.0
 tempxz=0.0
 #dotcolor = 0
 for iters in range(n):
  xz2 = xz*xz
  yz2 = yz*yz
  if xz2+yz2 > 4.0:
   #dotcolor = iters
   break

  tempxz = xz2-yz2+x
  yz=2.0*xz*yz+y
  xz=tempxz
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

  z = complex(x,y)
  o = complex(0,0)
  dotcolor = fractalpoint(xp,yp,n)
  im.putpixel((x,mySize[1]-y-1),dotcolor)

im.save("myfractal.gif")

longString1 = im.getdata()
longString2 = im2.getdata()

j=0
for i in range(len(longString1)):
 if longString1[i] <> longString2[i]:
  print chr(longString2[i]),
  j = j + 1
 if j > 1700:
  break

print
print j
