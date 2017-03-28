import re

myFile = file('equality.txt','r')
 
LongString = myFile.read()

s = re.findall('[a-z][A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]', LongString)
t=''
for i in range(10):
 t = t + s[i][4]

print t

