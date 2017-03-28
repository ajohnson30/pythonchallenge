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


im = Image.open("maze.png")
im2 = Image.new("RGB",(641,641))
myList = []

imdata = im.getdata()

print im.getpixel((640,0))
print im.getpixel((639,0))
print im.getpixel((637,3))

x=639
y=0

fw=2

ii = 0
cnt=0

while (y < 640):
 rt = operator.mod(fw-1,4)
 lt = operator.mod(fw+1,4)
 bw = operator.mod(fw+2,4)

 d = mydir(rt)
 p = im.getpixel((x+d[0],y+d[1]))
 #if (p[0] > 0) and (p[0] < 255):
  #print p[0]

 if p[2] == 0:
  im.putpixel((x,y),(p[0],p[1],240,p[3]))
  im2.putpixel((x,y),(p[0],p[1],240,p[3]))
  if p[0]>0:
   myList.append([x,y,p[0]])
  x = x + d[0]
  y = y + d[1]
  fw = rt
  ii = ii + 1
 elif p[2] == 240:
  im.putpixel((x,y),(p[0],p[1],120,p[3]))
  im2.putpixel((x,y),(0,0,0,0))
  if p[0]>0:
   #print myList
   #print str(x) + "," + str(y) + "," + str(p[0])
   try: 
    myList.remove([x,y,p[0]])
   except:
    #print "right removal failure"
    x=x
  x = x + d[0]
  y = y + d[1]
  fw = rt
  ii = ii - 1
 else:
  d = mydir(fw)
  p = im.getpixel((x+d[0],y+d[1]))
  
  if p[2] == 0:
   im.putpixel((x,y),(p[0],p[1],240,p[3]))
   im2.putpixel((x,y),(p[0],p[1],240,p[3]))
   if p[0]>0:
    myList.append([x,y,p[0]])
   x = x + d[0]
   y = y + d[1]
   ii = ii + 1
  elif p[2] == 240:
   im.putpixel((x,y),(p[0],p[1],120,p[3]))
   im2.putpixel((x,y),(0,0,0,0))
   if p[0]>0:
    #print myList
    #print str(x) + "," + str(y) + "," + str(p[0])
    try: 
     myList.remove([x,y,p[0]])
    except:
     #print "forward removal failure"
     x=x
   x = x + d[0]
   y = y + d[1]
   ii = ii - 1

  else:
   d = mydir(lt)
   p = im.getpixel((x+d[0],y+d[1]))
   if p[2] == 0:
    im.putpixel((x,y),(p[0],p[1],240,p[3]))
    im2.putpixel((x,y),(p[0],p[1],240,p[3]))
    if p[0]>0:
     myList.append([x,y,p[0]])
    x = x + d[0]
    y = y + d[1]
    fw = lt
    ii = ii + 1
   elif p[2] == 240:
    im.putpixel((x,y),(p[0],p[1],120,p[3]))
    im2.putpixel((x,y),(0,0,0,0))
    if p[0]>0:
     #print myList
     #print str(x) + "," + str(y) + "," + str(p[0])
     try: 
      myList.remove([x,y,p[0]])
     except:
      #print "left removal failure"
      x=x
    x = x + d[0]
    y = y + d[1]
    fw = lt
    ii = ii - 1
   else:
    d = mydir(bw)
    fw = bw
    im.putpixel((x,y),(p[0],p[1],120,p[3]))
    im2.putpixel((x,y),(0,0,0,0))
    if p[0]>0:
     #print myList
     #print str(x) + "," + str(y) + "," + str(p[0])
     try: 
      myList.remove([x,y,p[0]])
     except:
      #print "backwards removal failure"
      x=x
    x = x + d[0]
    y = y + d[1]
    ii = ii - 1
 cnt=cnt+1
 #print str(x) + "," + str(y) + " " + str(fw) + " " + str(p[1])


 if operator.mod(cnt,10000) == 0:
  print str(x) + "," + str(y) + " " + str(fw) + " " + str(p[1])

p = im.getpixel((x,y))
im.putpixel((x,y),(p[0],p[1],240,p[3]))
im2.putpixel((x,y),(p[0],p[1],240,p[3]))

im.save("maze2.png")
im2.save("maze3.png")
print ii
print myList

myFile=file('mazedump.txt','wb')
for i in range(len(myList)):
 myFile.write(chr(myList[i][2]))

myFile.close()
