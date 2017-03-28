import urllib
import Cookie
import httplib
import string
import base64 

userid = 'butter'
passwd = 'fly'

auth = 'Basic ' + string.strip(base64.encodestring(userid + ':' + passwd)) 



k = 30203


for ii in range(100):
 conn = httplib.HTTPConnection("www.pythonchallenge.com",80)
 conn.putrequest("GET", "/pc/hex/unreal.jpg")
 conn.putheader('Authorization', auth) 
 conn.putheader('Range','bytes=' + str(k) + '-')
 conn.endheaders()
 r1 = conn.getresponse()
 #print r1.status, r1.reason
 headers1 = r1.getheaders()
 #print headers1
 data1 = r1.read()
 print data1

 j=-1
 for i in range(len(headers1)):
  if headers1[i][0]=='content-range':
   j=i

 if j==-1:
  break

 s1 = headers1[j][1]

 i=s1.find('-')
 j=s1.find('/')

 k = int(s1[i+1:j])+1

conn.close()


k = 2123456789


for ii in range(100):
 conn = httplib.HTTPConnection("www.pythonchallenge.com",80)
 conn.putrequest("GET", "/pc/hex/unreal.jpg")
 conn.putheader('Authorization', auth) 
 conn.putheader('Range','bytes=' + str(k) + '-')
 conn.endheaders()
 r1 = conn.getresponse()
 #print r1.status, r1.reason
 headers1 = r1.getheaders()
 #print headers1
 data1 = r1.read()
 print data1

 j=-1
 for i in range(len(headers1)):
  if headers1[i][0]=='content-range':
   j=i

 if j==-1:
  break

 s1 = headers1[j][1]

 i=s1.find(' ')
 j=s1.find('-')

 k = int(s1[i+1:j])-1

conn.close()

k =  1152983631

conn = httplib.HTTPConnection("www.pythonchallenge.com",80)
conn.putrequest("GET", "/pc/hex/unreal.jpg")
conn.putheader('Authorization', auth) 
conn.putheader('Range','bytes=' + str(k) + '-')
conn.endheaders()
r1 = conn.getresponse()
#print r1.status, r1.reason
headers1 = r1.getheaders()
print headers1
data1 = r1.read()
print len(data1)
conn.close()

myFile = open("puzzle20.txt","wb")
myFile.write(data1)
myFile.close()



