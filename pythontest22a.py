import Image
import ImageEnhance
import gifmaker

im = Image.open("white.gif")

myFile = open("white2.gif","wb")

sequence = []


for i in range(132):
 im.seek(i)
 enh = ImageEnhance.Brightness(im)
 sequence.append(enh.enhance(250))

print len(sequence)
gifmaker.makedelta(myFile,sequence)
myFile.close()
