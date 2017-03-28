import Image
import operator

im = Image.open("mozart.gif")
im2 = Image.new('P',(640,480))

mypal = im.getpalette()

im2.putpalette(mypal)

j = 0

for y in range(480):
 newx=0;newy=0
 for x in range(640):
  i = im.getpixel((x,y))
  if i == 195:
   if j == 0:
    newx=x
    j = 1
  else:
   j = 0

 for x in range(640):
  i = im.getpixel((operator.mod(x+newx,640),y))
  im2.putpixel((x,y),i)

im2.save('mozart2.gif')
