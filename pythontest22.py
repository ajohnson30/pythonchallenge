import urllib
import Cookie
import httplib
import string
import base64 

userid = 'butter'
passwd = 'fly'

auth = 'Basic ' + string.strip(base64.encodestring(userid + ':' + passwd)) 


nexturl = 'http://butter:fly@www.pythonchallenge.com/pc/hex/white.gif'

myFile = urllib.urlopen(nexturl)
headers = myFile.info() 
print headers
LongString = myFile.read()
#print LongString
print len(LongString)
myFile.close()

myFile = open("white.gif","wb")
myFile.write(LongString)
myFile.close()

