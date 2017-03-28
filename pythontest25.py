import urllib
import wave
import chunk
import operator
import Image

im = Image.new("RGB",(300,300))

for i in range(25):
 s = str(i+1)
 fname = 'lake' + s + '.wav'
 print "retrieving wave file #" + s

 nexturl = 'http://www.pythonchallenge.com/pc/hex/' + fname
 myFile = urllib.urlopen(nexturl)
 LongString = myFile.read()
 myFile.close()
 myFile = open(fname,"wb")
 myFile.write(LongString)
 myFile.close()

 myFile = wave.open('lake' + s + ".wav","rb")
 mynframes = myFile.getnframes()
 myData = myFile.readframes(mynframes)
 myFile.close()

 print "writing picture piece #" + str(i+1)
 yy = (i/5)*60
 xx = operator.mod(i,5)*60

 for j in range(len(myData)/3):
  y = int(j/60) + yy
  x = operator.mod(j,60) + xx
  im.putpixel((x,y),(ord(myData[j*3]),ord(myData[j*3+1]),ord(myData[j*3+2]),255))

im.save("lake2.png")
