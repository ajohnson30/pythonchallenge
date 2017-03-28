import Image
import array

im = Image.open("oxygen.png")

imdata = im.getdata()
m = ''
print imdata

for i in range(87):
 j = im.getpixel((i*7,43))
 m = m + chr(j[0])

print m

j = m.find('[')

n = m[j+1:100].rstrip(']')

print n
print n[0]
j = n.split(',')

print j

k = len(j)
m=''
for i in range(k):
 m = m + chr(int(j[i]))
 

print m
