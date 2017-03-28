myFile = file('evil2.gfx','rb')
myFile1 = file('evil1.bmp','wb')
myFile2 = file('evil2.bmp','wb')
myFile3 = file('evil3.bmp','wb')
myFile4 = file('evil4.bmp','wb')
myFile5 = file('evil5.bmp','wb')

i = myFile.read(1)


while i <> '':
 myFile1.write(i)
 i = myFile.read(1)
 myFile2.write(i)
 i = myFile.read(1)
 myFile3.write(i)
 i = myFile.read(1)
 myFile4.write(i)
 i = myFile.read(1)
 myFile5.write(i)
 i = myFile.read(1)

