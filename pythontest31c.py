import Image 

im = Image.open('myfractal.gif',"r")
im2 = Image.open('mandelbrot.gif',"r")

longString1 = im.getdata()
longString2 = im2.getdata()

j=0
s=''
t=''
for i in range(len(longString1)):
 if longString1[i] <> longString2[i]:
  s = s + chr(longString2[i])
  t = t + chr(longString1[i])
  j = j + 1
  if j%73 == 0:
   print s
   print t
   s = ''
   t = ''
 if j > 1700:
  break

print
print j

#1679 is 73 x 23

