import Image
import operator

im = Image.open("cave.jpg")

im2 = Image.new("RGB",(640,480))
im3 = Image.new("RGB",(640,480))
im4 = Image.new("RGB",(640,480))
im5 = Image.new("RGB",(640,480))
im6 = Image.new("RGB",(640,480))

for y in range(480):
 for x in range(640):
  if operator.mod(y,2) == 0:
   if operator.mod(x,2) == 0:
    im2.putpixel((x,y),im.getpixel((x,y)))
    im6.putpixel((x,y),im.getpixel((x,y)))
   else:
    im3.putpixel((x,y),im.getpixel((x,y)))
  else:
   if operator.mod(x,2) == 0:
    im4.putpixel((x,y),im.getpixel((x,y)))
   else:
    im5.putpixel((x,y),im.getpixel((x,y)))
    im2.putpixel((x,y),im.getpixel((x,y)))

im2.save("cave1.bmp")
im3.save("cave2.bmp")
im4.save("cave3.bmp")
im5.save("cave4.bmp")
im6.save("cave5.bmp")

