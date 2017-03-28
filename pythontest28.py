import Image
import array
import operator

def myHex(h):
 ii = hex(h)[2:]
 if len(ii) < 2:
  ii = '0' + ii
 return ii


im = Image.open("bell.png")
im2 = Image.new("RGB",(320,480))

print "Image size is",im.size

h = im.size[1]
w = im.size[0]

idata = im.getdata()

print (len(idata)/2)

c = 42
k=0
l=[]
m=[]
n=[]
o=[]
p=""
q=[]
for x in range(len(idata)/2):
 if operator.mod(x+1,1000)==0:
  print (x+1),chr(13),

 j = idata[x*2+1][1] - idata[x*2][1]
 o.append(j)

 if j <> 42 and j <> -42:
  q.append(j)
 
 if j > 0:
  p = p + "0"
 else:
   p = p + "1"

 if c == j:
  k = k + 1
 else:
  l.append(k)
  if c > 0:
   m.append(k)
  else:
   n.append(k)
  k = 1
  c = j
    
myFile = open("ringring.txt","w")
for i in range(len(o)):
 if o[i] > 0:
  myFile.write(" " + str(o[i]) + ",")
 else:
  myFile.write(str(o[i]) + ",")

 if operator.mod(i,320) == 319:
  myFile.write(chr(13) + chr(10))
myFile.close()

myFile = open("ringring1.txt","w")
myFile.write(str(l))
myFile.close()

myFile = open("ringring2.txt","w")
myFile.write(str(m))
myFile.close()

myFile = open("ringring3.txt","w")
myFile.write(str(n))
myFile.close()

myFile = open("ringring4.txt","w")
myFile.write(p)
myFile.close()


myFile = open("ringring4a.txt","w")
myFile2 = open("ringring4b.txt","w")
for i in range(len(p)/8):
 n = int(p[i*8:i*8+8],2)
 myFile.write(str(n) + ", ")
 myFile2.write(chr(n))
myFile.close()
myFile2.close()
 

print q
