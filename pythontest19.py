import wave
import chunk


myFile = wave.open("indian.wav","rb")
myframerate = myFile.getframerate()
mynframes = myFile.getnframes()
mysamplewidth = myFile.getsampwidth()
mynchannels = myFile.getnchannels()

myData = myFile.readframes(mynframes)

myFile.close()

print 'framerate: ' + str(myframerate)
print '# frames: ' + str(mynframes)
print 'sample width: ' + str(mysamplewidth)
print '# channels: ' + str(mynchannels)
print 'data length: ' + str(len(myData))

myData2=''
for i in range((len(myData)/2)):
 myData2 = myData2 + myData[i*2+1] + myData[i*2]

myFile = wave.open("indian2.wav","wb")
myFile.setnchannels(mynchannels)
myFile.setsampwidth(mysamplewidth)
myFile.setframerate(myframerate)
myFile.writeframes(myData2)
myFile.close()
