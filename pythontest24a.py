import Image
import operator
import sys

global ii

sys.setrecursionlimit(50000)


im = Image.open("maze.png")

imdata = im.getdata()

x=639
y=0

dir=2
ii=0


def checkspot(x,y,d):
 global ii
 global im

 ii = ii + 1
 print ii

 if y==640:
  return 1

 r = operator.mod(d-1,4)
 l = operator.mod(d+1,4)
 solved = 0

 p=im.getpixel((x+mydir(d)[0],y+mydir(d)[1]))
 if p[1]==0:
  if checkspot(x+mydir(d)[0],y+mydir(d)[1],d)==1:
   im.putpixel((x,y),(p[0],p[1],240,p[3]))
   solved = 1

 if solved == 0:
  p=im.getpixel((x+mydir(r)[0],y+mydir(r)[1]))
  if p[1]==0:
   if checkspot(x+mydir(r)[0],y+mydir(r)[1],r)==1:
    im.putpixel((x,y),(p[0],p[1],240,p[3]))
    solved = 1

 if solved == 0:
  p=im.getpixel((x+mydir(l)[0],y+mydir(l)[1]))
  if p[1]==0:
   if checkspot(x+mydir(l)[0],y+mydir(l)[1],l)==1:
    im.putpixel((x,y),(p[0],p[1],240,p[3]))
    solved = 1
 return 0

def mydir(d):
 if d==0:
  return (0,-1)
 elif d==1:
  return (1,0)
 elif d==2:
  return (0,1)
 return (-1,0)


checkspot(x,y,dir)

im.save("maze2.png")


