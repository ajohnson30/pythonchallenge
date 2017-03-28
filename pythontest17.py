import urllib2
import Cookie
#import cookielib, urllib2

#cj = cookielib.CookieJar()
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#r = opener.open(nexturl)


#myFile = urllib2.urlopen('http://www.pythonchallenge.com//pc/return/romance.html')
#headers = myFile.info() 
#cookie = headers.getheader("set-cookie") 
#c = Cookie.SimpleCookie(cookie)
#print c["info"].value



nexturl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345'
n = '12345'
o = 12345
p = ''

myFile = urllib2.urlopen(nexturl)
headers = myFile.info() 
cookie = headers.getheader("set-cookie") 
c = Cookie.SimpleCookie(cookie)
print c["info"].value
p = p + c["info"].value
count = 1

LongString = myFile.read()

print LongString

j = LongString.find('next busynothing is')
print j
print LongString[j:1000]
m = LongString[j+20:1000]
print m
n = n + m
print n
o = o + int(m)

nexturl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=' + m

for i in range(300):
 count = count + 1
 myFile = urllib2.urlopen(nexturl)
 headers = myFile.info() 
 cookie = headers.getheader("set-cookie") 
 c = Cookie.SimpleCookie(cookie)
 print c["info"].value
 p = p + c["info"].value
 #print c["info"].coded_value
 
 LongString = myFile.read()
 
 myFile.close()
 print LongString

 j = LongString.find('next busynothing is')

 if j == -1:
  break
 m = LongString[j+20:100]
 n = n + m
 o = o + int(m)

 nexturl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=' + m

print count
print n
print len(n)
print o
print p
