ulx=-2.0
uly=1.0
lrx=1.0
lry=-1.0

w=75
h=36

max=100

y=uly
while y>lry:
   x=ulx
   line=""
   while x<lrx:
      c=complex(x,y)
      z=0+0j
      iter=0
      while abs(z)<2 and iter<max:
         z=z*z+c
         iter=iter+1

      if iter<max:
         line=line+" "
      else:
         line=line+"#"
      
      x=x+(lrx-ulx)/w

   print line
   y=y+(lry-uly)/h

