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


pattern=[]
for i in range(dx):
 pattern.append([0]*dy)


count = 0

def printfigure(pat):
 for y in range(dy):
  s=""
  for x in range(dx):
   if pat[y][x]==0:
    s=s+" "
   else:
    s=s+"X"
  print s
 print

def checkfigure(pat):
 match=1
 for y in range(len(pat)):
  t=[]
  for i in str(pat[y]).strip('[]').replace(', ','').split('0'):
   if i<>'':
    t=t+[len(i)]
  if t<>mv[y]:
   match=0

 if match==1:
  return True
 return False


def placeblock(y,n,p,s,pat):
 global count


 for j in range(s+1):
  for k in range(dy-p):
   #pat[y][k+p]=0
   pat[k+p][y]=0

  for k in range(mh[y][n]):
   #pat[y][k+j+p]=1
   pat[k+j+p][y]=1

  #u = t + (" "*(j+1)) + "X"*mh[y][n]
  if n < len(mh[y])-1:
   placeblock(y,n+1,p + j + mh[y][n]+1,s-j,pat)
  else:
   #g = f + string.ljust(u,dx+1) + chr(10)
   if y<dy-1:
    s = dx - (sum(mh[y+1])+len(mh[y+1])-1)
    placeblock(y+1,0,0,s,pat)
    #print pat[0]
   else:
    count = count + 1
    if count%1000==0:
     print count,chr(13),
    if checkfigure(pat)==True:
     printfigure(pat)

 

print time.ctime(time.time())
i = mh[0]
spacesleft = dx - (sum(i)+len(i)-1)

placeblock(0,0,0,spacesleft,pattern)

print count
print time.ctime(time.time())

#myFile.close()

