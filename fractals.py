# A simple fractals program by Kirby Urner
# Latest version:  Sept 25, 2004 -- added image palette for color

from __future__ import division # needed pre 2.4 (?)
import Image  # PIL installed under site-packages
import ImagePalette

# put your preferred path for saving files here:
mypath = './'  

def mkpalette():
    global palette
    palette = [0,0,0]
    
    for i in range(0,255):
        palette.extend((i*5%200 + 55, i*7%200 + 55, i*11%200 + 55))        
    return palette

class Julia:

    def __init__(self, filename, size, n=64, box=((-2,1.25),(0.5,-1.25)) ):
        self.size = size
        self.filename = filename
        self.n = n
        self.uleft  = box[0]
        self.lright = box[1]
        self.xwidth = self.lright[0] - self.uleft[0]
        self.ywidth = self.uleft[1]  - self.lright[1]

    def __call__(self,z):
        self.z = z
        self.compute()
                        
    def newimage(self):
        self.im = Image.new('P',self.size)
        self.im.putpalette(mkpalette())

    def compute(self):
        print "Computing %s..." % self.__class__.__name__
        self.newimage()
        i = 0
        j = 0
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                xp,yp = self.getcoords(x,y)                
                dotcolor = self.fractal(xp,yp)
                if dotcolor != i:
                 print dotcolor,
                 j = j + 1
                 i = dotcolor
                self.im.putpixel((x,y),dotcolor)
        self.saveimage()
        print
        print j

    def fractal(self,x,y):
        n = self.n
        z = self.z
        o = complex(x,y)
        dotcolor = 0  # default, convergent
        for trials in range(n):
            if abs(o) <= 2.0:
                o = o**2 + z
            else:
                dotcolor = trials
                break  # diverged
        return dotcolor            

    def getcoords(self,x,y):
        percentx = x/self.size[0]
        percenty = y/self.size[1]
        xp = self.uleft[0] + percentx * (self.xwidth)
        yp = self.uleft[1] - percenty * (self.ywidth)
        return (xp,yp)
    
    def saveimage(self):
        self.im.save(self.filename)
                

class Mandelbrot(Julia):

    def fractal(self,x,y):
        n = self.n
        z = complex(x,y)
        o = complex(0,0)
        dotcolor = 0  # default, convergent
        for trials in range(n):
            if abs(o) <= 2.0:
                o = o**2 + z
            else:
                dotcolor = trials
                break  # diverged
        return dotcolor
                    
def test():
    f = Julia(mypath + 'julia.png',(500,500), n=128, box=((-1.2,1.2),(1.2,-1.2)) )
    f(complex(-0.74543,0.11301))
    f = Mandelbrot(mypath + 'mandelbrot.png',(500,500))
    f.compute()
    
if __name__ == '__main__':
    test()

