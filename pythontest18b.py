import difflib
import string
import zlib
import gzip
import binascii

myFile = file('delta.txt','r')
myData = myFile.readlines()
myFile.close()

s1=''
s2=''

for i in range(len(myData)):
 ss1 = string.strip(myData[i][0:53])
 ss2 = string.strip(myData[i][56:109])
 if len(ss1) > 0:
  s1 = s1 + ss1 + chr(13) + chr(10)
 if len(ss2) > 0:
  s2 = s2 + ss2 + chr(13) + chr(10)

ss3 = s1.splitlines()
ss4 = s2.splitlines()

print 'creating diff list'
result = difflib.Differ().compare(ss3,ss4)
result3 = chr(13).join(result)
result2 = result3.splitlines()

myFile = file('deltas0.txt','wb')
myFile.write(result3)
myFile.close()

d1=''
d2=''
d3=''

print 'splitting list'

for i in range(len(result2)):
 myLine=string.strip(result2[i])
 c=''
 if len(myLine) > 1:
  c=myLine[0]

 if c=='-':
  d1 = d1 + myLine[2:60] + ' '
 elif c=='+':
  d2 = d2 + myLine[2:60] + ' '
 else:
  d3 = d3 + myLine[0:53] + ' '

print 'saving files'

myFile = file('deltas1.png','wb')
ss1 = string.split(d1)
for i in range(len(ss1)):
 if len(ss1[i])==2:
  myFile.write(chr(int(ss1[i],16)))
myFile.close()

myFile = file('deltas2.png','wb')
ss1 = string.split(d2)
for i in range(len(ss1)):
 if len(ss1[i])==2:
  myFile.write(chr(int(ss1[i],16)))
myFile.close()

myFile = file('deltas3.png','wb')
ss1 = string.split(d3)
for i in range(len(ss1)):
 if len(ss1[i])==2:
  myFile.write(chr(int(ss1[i],16)))
myFile.close()


