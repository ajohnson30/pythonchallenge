import  cookielib, urllib2, Cookie
cj = cookielib.MozillaCookieJar()
cj.load("C:\Documents and Settings\\ajohnson\Desktop\Development Stuff\pythonchallenge\cookie\\cookies.txt")
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
myFile = opener.open("http://www.pythonchallenge.com/pc/stuff/violin.php")
headers = myFile.info() 
print
print 'headers'
print headers
cookie = headers.getheader("set-cookie") 
c = Cookie.SimpleCookie(cookie)
print
print 'cookie'
print c
