import zlib
import bz2
import array

myFile = open('level21/package.pack','rb')
LongString = myFile.read()
myFile.close()

ll = '['
for j in range(200):
 print j
 ll = ll + '['

 for k in range(200):
  print ' ' + str(k)
  i1 = 0
  for i in range(20):
   if LongString[0]<>'x' and LongString[1]<>'£':
    break
   i1=i1+1
   data = zlib.decompress(LongString)
   LongString = data
  print '  ' + str(i)
 
  i2 = 0
  for i in range(20):
   if LongString[0]<>'B' and LongString[1]<>'Z':
    break
   i2=i2+1
   data = bz2.decompress(LongString)
   LongString = data
  print '  ' + str(i)
  #ll = ll + '[' + str(i1+1) + ',' + str(i2+1) + '],'
  ll = ll + '[' + str(i1) + ',' + str(i2) + '],'
  if LongString[0]<>'x' and LongString[1]<>'£':
   ll = ll[0:len(ll)-1] + '],'
   break

 l = len(LongString)
 if LongString[l-1]<>'x' and LongString[l-2]<>'£':
  break

 data = ''
 for i in range(len(LongString)):
  data = data + LongString[len(LongString)-i-1]
 LongString = data

print len(LongString)
print LongString
data = ''
for i in range(len(LongString)):
 data = data + LongString[len(LongString)-i-1]
LongString = data
print len(LongString)
print LongString

ll = ll[0:len(ll)-1] + ']'

print ll

myList = eval(ll)


print myList[0]
print myList[0][0]
print myList[0][0][0]

print len(myList)
print len(myList[0])

myFile = open('python21.txt','w')
for i in range(len(myList)):
 ss=''
 for j in range(len(myList[i])):
  for k in range(myList[i][j][0]):
   ss = ss + ' '
  for k in range(myList[i][j][1]):
   ss = ss + '*'
 print ss
 myFile.write(ss + chr(13) + chr(10))

myFile.close()


