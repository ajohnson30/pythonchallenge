from Tkinter import * 
import Image
import ImageTk


def myHex(h):
 ii = hex(h)[2:]
 if len(ii) < 2:
  ii = '0' + ii
 return ii

def maxpixels(i):
 m=0
 n=0
 for j in range(len(i)):
  if i[j]>m:
   m=i[j]
   n=j
 return n

im = Image.open("beer2.png","r")

hist = im.histogram()

im2 = Image.new("L",(138,138))

for y in range(138):
 for x in range(137):
   im2.putpixel((x,y),255)


class myApp: 
    pos = 0
    def __init__(self, root): 
        self.root = root 


        self.photo = ImageTk.PhotoImage(im2)
        self.canvas = Canvas(self.root, width=400, height=400) 
        self.canvas.create_image(1, 1, anchor=NW, image=self.photo) 
        self.canvas.photo = self.photo # must keep a reference!!! 
        self.canvas.pack() 
        self.root.after(1000, self.myLoop)



    def myLoop(self): 
        # Because bind gives an argument, which I will always need, but 
        # after doesn't give the argument. 

        print self.pos,chr(13),
        self.pos = self.pos + 1

        p = maxpixels(hist)
        for y in range(138):
         for x in range(138):
          if im.getpixel((x,y)) == p:
           im2.putpixel((x,y),0)
        hist[p]=0
        self.photo = ImageTk.PhotoImage(im2)
        self.canvas.create_image(1, 1, anchor=NW, image=self.photo) 
        self.canvas.photo = self.photo # must keep a reference!!! 
        self.canvas.pack() 


        if self.pos < 66:
         self.root.after(1000, self.myLoop) 


root = Tk() 
root.title('33 beers') 
myApp(root)
mainloop()
