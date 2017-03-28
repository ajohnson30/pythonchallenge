import urllib
import Cookie
import httplib
import string
import base64 

userid = 'butter'
passwd = 'fly'

auth = 'Basic ' + string.strip(base64.encodestring(userid + ':' + passwd)) 


nexturl = 'http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg'

myFile = urllib.urlopen(nexturl)
headers = myFile.info() 
print headers
LongString = myFile.read()
#print LongString
print len(LongString)
myFile.close()

#myFile = open("unreal2.jpg","wb")
#myFile.write(LongString)
#myFile.close

conn = httplib.HTTPConnection("www.pythonchallenge.com",80)
conn.putrequest("GET", "/pc/hex/unreal.jpg")
conn.putheader('Authorization', auth) 
conn.endheaders()

r1 = conn.getresponse()
print r1.status, r1.reason
headers1 = r1.getheaders()
data1 = r1.read()
print len(data1)
#print headers1
conn.close()


conn = httplib.HTTPConnection("www.pythonchallenge.com",80)
conn.putrequest("GET", "/pc/hex/unreal.jpg")
conn.putheader('Authorization', auth) 
conn.putheader('Range','bytes=30203-30303')
conn.endheaders()
r1 = conn.getresponse()
print r1.status, r1.reason
headers1 = r1.getheaders()
data1 = r1.read()
print data1
myrange = headers1.index('Content-Range')
print headers1[myrange][1]

conn.close()



