import difflib
import string
import zlib
import gzip
import binascii

myFile = file('delta.txt','r')

myData = myFile.readlines()

myFile.close()


l = len(myData)

s1=''
s2=''
s3=''
s4=''

for i in range(len(myData)):
 ss1 = string.strip(myData[i][0:53])
 ss2 = string.strip(myData[i][56:109])
 if len(ss1) > 0:
  s1 = s1 + ss1 + ' '
  s3 = s3 + ss1 + chr(13) + chr(10)
 if len(ss2) > 0:
  s2 = s2 + ss2 + ' '
  s4 = s4 + ss2 + chr(13) + chr(10)

ss3 = s3.split(chr(13))
ss4 = s4.split(chr(13))


myFile1 = file('deltas1.png','wb')
ss1 = string.split(s1)
for i in range(len(ss1)):
 myFile1.write(chr(int(ss1[i],16)))
myFile1.close()

myFile2 = file('deltas2.png','wb')
ss2 = string.split(s2)
for i in range(len(ss2)):
 myFile2.write(chr(int(ss2[i],16)))
myFile2.close()

print 'done with png files'
print


print 'creating diff list'
#result = difflib.Differ()
result = difflib.ndiff(ss3,ss4)
#result = difflib.context_diff(ss3,ss4)
#result = difflib.unified_diff(ss3,ss4)
#result = difflib.Differ().compare(ss3,ss4)

result3 = ''.join(result)
result2 = result3.split(chr(10))


d1=''
d2=''
d3=''
d4=''
d5=''
d6=''

crlf = chr(13) + chr(10)

print 'splitting list'
myFile = file('deltas0.txt','wb')

for i in range(len(result2)):
 myFile.write(string.strip(result2[i]) + crlf)
 myLine=string.strip(result2[i])
 d6 = d6 + myLine[0:53] + crlf
 c=''
 if len(myLine) > 1:
  c=myLine[len(myLine)-1]

 if c=='-':
  d1 = d1 + myLine[0:53] + crlf
  d4 = d4 + myLine[0:53] + crlf
 elif c=='+':
  d2 = d2 + myLine[0:53] + crlf
  d5 = d5 + myLine[0:53] + crlf
 else:
  d3 = d3 + myLine[0:53] + crlf
  d4 = d4 + myLine[0:53] + crlf
  d5 = d5 + myLine[0:53] + crlf
myFile.close()

print 'saving files'

myFile = file('deltas1.txt','wb')
myFile.write(d1)
myFile.close()

myFile = file('deltas2.txt','wb')
myFile.write(d2)
myFile.close()

myFile = file('deltas3.txt','wb')
myFile.write(d3)
myFile.close()

myFile = file('deltas4.txt','wb')
myFile.write(d4)
myFile.close()

myFile = file('deltas5.txt','wb')
myFile.write(d5)
myFile.close()

myFile = file('deltas6.txt','wb')
myFile.write(d6)
myFile.close()

myFile = file('deltas3.png','wb')
ss1 = string.split(d3)
for i in range(len(ss1)):
 if len(ss1[i])==2:
  myFile.write(chr(int(ss1[i],16)))
myFile.close()

myFile = file('deltas4.png','wb')
ss1 = string.split(d4)
for i in range(len(ss1)):
 if len(ss1[i])==2:
  myFile.write(chr(int(ss1[i],16)))
myFile.close()

myFile = file('deltas5.png','wb')
ss1 = string.split(d5)
for i in range(len(ss1)):
 if len(ss1[i])==2:
  myFile.write(chr(int(ss1[i],16)))
myFile.close()

myFile = file('deltas6.png','wb')
ss1 = string.split(d6)
for i in range(len(ss1)):
 if len(ss1[i])==2:
  myFile.write(chr(int(ss1[i],16)))
myFile.close()

