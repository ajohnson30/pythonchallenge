import Image
import ImageEnhance
import gifmaker

im = Image.open("white.gif")
im2 = Image.new("RGB",(200,200))

myx = 0
myy = 100

mychar = 0

for i in range(132):
 im.seek(i)

 xx = 0
 yy = 0

 for y in range(200):
  for x in range(200):
   s = im.getpixel((x,y))
   if s > 0:
    print 'image #' + str(i) + ' has ' + str(s) + ' at (' + str(x) + ',' + str(y) + ')'
    xx = x - 100
    yy = y - 100

 if (xx == 0) and (yy == 0):
  mychar = mychar + 1
  myx = mychar * 30
  myy = 100
 else:
  myx = myx+xx
  myy = myy+yy
 im2.putpixel((myx,myy),255)

im2.save('white3.gif')
