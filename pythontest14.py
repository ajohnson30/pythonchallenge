import Image
import array

im = Image.open("wire.png")
im2 = Image.new('RGB',(100,100))

dir = 1
x=0
y=0
minx = 0
miny = 1
maxx = 99
maxy = 99

for i in range(10000):
 im2.putpixel((x,y),im.getpixel((i,0)))
 if dir == 1:
  x = x+1
  if x > maxx:
   x = maxx
   maxx = maxx - 1
   dir = 2
   y = y+1
   print x
 
 elif dir == 2:
  y = y+1
  if y > maxy:
   y = maxy
   maxy = maxy - 1
   dir = 3
   x = x-1
   print y
 elif dir == 3:
  x = x-1
  if x <  minx:
   x = minx
   minx = minx + 1
   dir = 4
   y = y-1
   print x

 elif dir == 4:
  y = y-1
  if y <  miny:
   y = miny
   miny = miny + 1
   dir = 1
   x = x+1
   print y
 

print str(x) + " " +  str(y)

im2.save('wire2.png')

