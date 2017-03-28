import time
import string

dx=32
dy=32
count = 0

mh = [[3,2],[8],[10],[3,1,1],
      [5,2,1],[5,2,1],[4,1,1],[15],
      [19],[6,14],[6,1,12],[6,1,10],
      [7,2,1,8],[6,1,1,2,1,1,1,1],[5,1,4,1],[5,4,1,4,1,1,1],
      [5,1,1,8],[5,2,1,8],[6,1,2,1,3],[6,3,2,1],
      [6,1,5],[1,6,3],[2,7,2],[3,3,10,4],
      [9,12,1],[22,1],[21,4],[1,17,1],
      [2,8,5,1],[2,2,4],[5,2,1,1],[5]]

mv = [[5],[5],[5],[3,1],
      [3,1],[5],[5],[6],
      [5,6],[9,5],[11,5,1],[13,6,1],
      [14,6,1],[7,12,1],[6,1,11,1],[3,1,1,1,9,1],
      [3,4,10],[8,1,1,2,8,1],[10,1,1,1,7,1],[10,4,1,1,7,1],
      [3,2,5,2,1,2,6,2],[3,2,4,2,1,1,4,1],[2,6,3,1,1,1,1,1],[12,3,1,2,1,1,1],
      [3,2,7,3,1,2,1,2],[2,6,3,1,1,1,1],[12,3,1,5],[6,3,1],
      [6,4,1],[5,4],[4,1,1],[5]]


#myFile = open("pythontest32a.txt","w")

def checkfigure2(f):
 s=""
 match=1
 for x in range(dx+1):
  for y in range(dy):
   s = s + f[y*(dx+2)+x]
  s=s+chr(10)

 ss=s.splitlines()

 for i in range(len(ss)-1):
  s2 = ss[i+1].strip().split(" ")

  t = []
  for j in s2:
   if j <> '':
    t = t + [len(j)]

  if t <> mv[i]:
   match=0
 if match==1:
  return True
 return False
  

def checkfigure(f):
 s = f.splitlines()
 
 match=1

 for x in range(dx):
  t=[]
  d = 0
  e = 0
  a=""
  for y in range(dy):
   a=a+s[y][x+1]
   if s[y][x+1]=="X":
    if e==0:
     e=1
    d=d+1
   else:
    if e==1:
     t = t + [d]
    e=0
    d=0
  if d > 0:
   t = t + [d]
  if t!=mv[x]:
   match=0
 
 if match==1:
  return True
 return False
  

def placeblock(y,i,n,s,t,f):
 global count
 for j in range(s+1):
  u = t + (" "*(j+1)) + "X"*i[n]
  if n < len(i)-1:
   placeblock(y,i,n+1,s-j,u,f)
  else:
   g = f + string.ljust(u,dx+1) + chr(10)
   if y<dy-1:
    k = mh[y+1]
    s = dx - (sum(k)+len(k)-1)
    placeblock(y+1,k,0,s,"",g)
   else:
    count = count + 1
    if count%1000==0:
     print count,chr(13),
    #myFile.write(str(count) + chr(10) + g + chr(10))
    if checkfigure2(g) == True:
     print count,chr(10) + time.ctime(time.time()) + chr(10) + g
 

print time.ctime(time.time())
i = mh[0]
spacesleft = dx - (sum(i)+len(i)-1)
print i,spacesleft,dx,count
placeblock(0,i,0,spacesleft,"","")
print count
print time.ctime(time.time())

#myFile.close()



