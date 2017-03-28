import urllib
import re
import zipfile

LongString = 'Next nothing is 90052'

j = LongString.find('Next nothing is')

m = LongString[j+16:100]

nextfile = 'zip/' + m + ".txt"

mycmnt = ''

for i in range(1000):

 myFile = file(nextfile,'r')
 n = zipfile.ZipFile('channel.zip','r').getinfo(m + '.txt').comment
 mycmnt = mycmnt + n
 
 LongString = myFile.read()
 
 myFile.close()
 print LongString
 print n
 j = LongString.find('Next nothing is')

 m = LongString[j+16:100]

 nextfile = 'zip/' + m + ".txt"

 if LongString.find('comments') > 0:
  break


print mycmnt
