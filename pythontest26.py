import md5
import array

goodDigest = "bbb8b499a0eef99b52c7f13f4e78c24b"

myFile = open("mybroken.zip","rb")

longString = array.array("c",myFile.read())

myFile.close()

i = -1
j = -1
for k in range(len(longString)):
 l = longString[k]
 for m in range(256):
  longString[k] = chr(m)
  if md5.new(longString).hexdigest() == goodDigest:
   i=k
   j=m
   print "Found bad byte at position " + str(k) + ", was " + str(hex(ord(l))) + " but should be " + str(hex(m))
   break
 if i >= 0:
  break
 longString[k]=l

if i >= 0:
 print "Writing new file"
 myFile = open("mybroken1.zip","wb")
 myFile.write(longString)
 myFile.close()
 
  
