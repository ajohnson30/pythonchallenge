#import urllib
import urllib2
import Cookie
#import ClientCookie


req1 = urllib2.Request("http://www.pythonchallenge.com/pc/stuff/violin.php") 
req1.add_header('Cookie','info=the flowers are on their way')

myFile = urllib2.urlopen(req1)

headers = myFile.info() 
print
print 'headers'
print headers
cookie = headers.getheader("set-cookie") 
c = Cookie.SimpleCookie(cookie)
print
print 'cookie'
print c
#print c["info"].value

LongString = myFile.read()
print LongString

