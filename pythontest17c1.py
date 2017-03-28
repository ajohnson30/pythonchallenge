import os, cookielib, urllib2, Cookie

cj = cookielib.CookieJar()
#c1=Cookie.SimpleCookie()
#c1["info"]='the flowers are on their way'
#cj.set_cookie(c1)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

myFile = opener.open("http://www.pythonchallenge.com/pc/def/linkedlist.php")
print cj

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

c["info"]='the flowers are on their way'
print c
#c["domain"]="pythonchallenge.com"
cj.set_cookie(c)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

myFile = opener.open("http://www.pythonchallenge.com/pc/stuff/violin.php")
print cj

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



