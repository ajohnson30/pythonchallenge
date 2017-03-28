import urllib
import re
import pickle
import string
import operator


nexturl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=2123456789'

myFile = urllib.urlopen(nexturl)
 
LongString = myFile.read()


j = LongString.find('next nothing is')

m = LongString[j+16:100]

nexturl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + m

for i in range(300):

 myFile = urllib.urlopen(nexturl)
 
 LongString = myFile.read()
 
 myFile.close()
 print LongString

 j = LongString.find('next nothing is')

 if j == -1:
  break

 m = LongString[j+16:100]

 nexturl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + m

nexturl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(int(m)/2)

for i in range(300):

 myFile = urllib.urlopen(nexturl)
 
 LongString = myFile.read()
 
 myFile.close()
 print LongString

 j = LongString.find('next nothing is')

 if j == -1:
  break

 m = LongString[j+16:100]

 nexturl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + m

