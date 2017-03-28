import urllib
import re
import pickle
import string
import operator


nexturl = 'http://www.pythonchallenge.com/pc/def/banner.p'

myFile = urllib.urlopen(nexturl)
 
LongString = myFile.read()
 
myFile.close()

m = pickle.loads(LongString)
print m
k=0
for i in m:
 s = ''
 for j in i:
  s = s + operator.repeat(j[0],j[1])
 print s

