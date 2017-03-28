import time
import string

dx=9
dy=9
count = 0

mh = [[2,1,2],[1,3,1],[5],[7],[9],[3],[2,3,2],[2,3,2],[2,3,2]]
mv = [[2,1,3],[1,2,3],[3],[8],[9],[8],[3],[1,2,3],[2,1,3]]

#xx  x  xx
#x  xxx  x
#  xxxxx
# xxxxxxx
#xxxxxxxxx
#   xxx
#xx xxx xx
#xx xxx xx
#xx xxx xx

#myFile = open("pythontest32.txt","w")
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

