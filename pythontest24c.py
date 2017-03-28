import Image
import operator

def mydir(d):
 if d==0:
  return (0,-1)
 elif d==1:
  return (1,0)
 elif d==2:
  return (0,1)
 return (-1,0)

im = Image.open("maze3.png")
myFile=file('mazedump2.txt','wb')

imdata = im.getdata()

print im.getpixel((640,0))
print im.getpixel((639,0))
print im.getpixel((637,3))

x=639
y=0

fw=2

ii=0
cnt=0

p = im.getpixel((x,y))

while (y < 640):
 rt = operator.mod(fw-1,4)
 lt = operator.mod(fw+1,4)

 if operator.mod(ii,2)==0:
  p = im.getpixel((x,y))
  myFile.write(chr(p[0]))

 d = mydir(rt)
 p = im.getpixel((x+d[0],y+d[1]))
 if p[2] > 0:
  x = x + d[0]
  y = y + d[1]
  fw = rt
  ii = ii + 1
 else:
  d = mydir(fw)
  p = im.getpixel((x+d[0],y+d[1]))
  if p[2] > 0:
   x = x + d[0]
   y = y + d[1]
   #fw = fw
   ii = ii + 1
  else:
   d = mydir(lt)
   p = im.getpixel((x+d[0],y+d[1]))
   if p[2] > 0:
    x = x + d[0]
    y = y + d[1]
    fw = lt
    ii = ii + 1
   else:
    
    print "ACK I got lost at " + str(x) + "," + str(y) + " after " + str(ii) + " steps"
    y = 640

 if operator.mod(ii,10000) == 0:
  print str(x) + "," + str(y) + " " + str(fw)

print ii

myFile.close()
