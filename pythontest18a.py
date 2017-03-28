import urllib


nexturl = 'http://www.pythonchallenge.com/pc/return/deltas.gz'

myFile = urllib.urlopen(nexturl)
 
LongString = myFile.read()

myFile2 = file("delta.gz","wb")
myFile2.write(LongString)
myFile2.close()
