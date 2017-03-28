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

print ss3


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
print result3
result2 = result3.split(chr(10))
