#==============================================================
# (c) John Whitehouse 2002-2003
# htpp://www.eddaardvark.co.uk/
#
# Draws Mandelbrots and Julia sets
#==============================================================

import WindowsBMP
import ColourMap
import time
import sys

from MakeFileList import MakeFileList

# Some co-ordinates used in the examples

interesting_coords = [  (-0.3006818, 0.6600910),
                        (-0.5511328, 0.627839636),
                        (0.27322626, 0.595153338),
                        (-0.1555049, 0.650170438),
                        (0.42661603, 0.217772923),
                        (-0.502875,  0.518925),
                        (-1.2583585, 0.3821136)]

# Default 'c' value

active_point=0

# position of black in the bitmap's colour table

BLACK_INDEX = chr(0)
BLACK       = chr(0)+chr(0)+chr(0)+chr(0)

#=================================================================
# The Mandelbrot Pattern class
#=================================================================

class Mandelbrot:

    def __init__ (self):
        self.path        = 'c:\\python22\\work\\'
        self.filename    = 'mandelbrot'
        self.xpos        = -0.5
        self.ypos        = 0
        self.scale       = 0.00375
        self.iterations  = 100
        self.draw        = self.drawStandard
        self.pfuns       = [self.pf1, self.pf2, self.pf3, self.pf4, self.pf5]
        self.julia_point = interesting_coords [active_point]
        self.starfactor  = 0.001
        self.palette     = 0
        self.z_start     = (0,0)

        self.setSize ((800, 600))
        self.buildColourMap (100)

#-----------------------------------------------------------------------
    def setSize (self, size):
        "Set the size"

        self.size = size

        self.bitmap = WindowsBMP.WindowsBMP ()
        self.bitmap.create8Bit (self.size [0], self.size [1])

#-----------------------------------------------------------------------
    def drawStandard(self):
        """
        Draw a mandelbrot based on the current values. Pattern is
        coloured according to the number of iterations before the
        value of abs(z) passes 2.
        """

        xmin    = self.xpos - self.scale * self.size [0] / 2
        ymin    = self.ypos - self.scale * self.size [1] / 2
        ilist   = range (0, self.iterations)
        ixrange = range (0, self.size [0])
        iyrange = range (0, self.size [1])
        xrange  = [xmin + self.scale * ix for ix in ixrange]
        yrange  = [ymin + self.scale * iy for iy in iyrange]

        z0 = complex (self.z_start [0], self.z_start [1])
        
        for ix in ixrange:
            for iy in iyrange:
                c = complex (xrange [ix],yrange [iy])
                z = z0
                colour = BLACK_INDEX
                
                for i in ilist:
                    z = z * z + c
                    if abs(z) >= 2:
                        colour = self.colour_map [i]
                        break

                self.bitmap.setPixel (ix, iy, colour)

#-----------------------------------------------------------------------
    def drawJulia(self):
        """
        Draw a Julia set based on the current values. Pattern is
        coloured according to the number of iterations before the
        value of abs(z) passes 2.
        """

        xmin    = self.xpos - self.scale * self.size [0] / 2
        ymin    = self.ypos - self.scale * self.size [1] / 2
        ilist   = range (0, self.iterations)
        ixrange = range (0, self.size [0])
        iyrange = range (0, self.size [1])
        xrange  = [xmin + self.scale * ix for ix in ixrange]
        yrange  = [ymin + self.scale * iy for iy in iyrange]

        c = complex (self.julia_point [0], self.julia_point [1])        
        
        for ix in ixrange:
            for iy in iyrange:
                z = complex (xrange [ix],yrange [iy])
                colour = BLACK_INDEX
                
                for i in ilist:
                    z = z * z + c

                    if abs(z) >= 2:
                        colour = self.colour_map [i]
                        break

                self.bitmap.setPixel (ix, iy, colour)

#-----------------------------------------------------------------------
    def drawStars(self):
        """
        Draw a mandelbrot based on the current values. Pattern is
        coloured according to how close the iterand gets to the origin before
        escaping.
        """

        xmin    = self.xpos - self.scale * self.size [0] / 2
        ymin    = self.ypos - self.scale * self.size [1] / 2
        ilist   = range (0, self.iterations)
        ixrange = range (0, self.size [0])
        iyrange = range (0, self.size [1])
        xrange  = [xmin + self.scale * ix for ix in ixrange]
        yrange  = [ymin + self.scale * iy for iy in iyrange]

        z0 = complex (self.z_start [0], self.z_start [1])        

        for ix in ixrange:
            for iy in iyrange:
                c = complex (xrange [ix],yrange [iy])
                z = z0
                colour = BLACK_INDEX
                mind = 2
                
                for i in ilist:
                    z = z * z + c
                    d = abs (z)
                    
                    if d >= 2:
                        n = int (mind/self.starfactor)
                        n = min (n, 254)
                        colour = chr(n+1)
                        break
                    else:
                        mind = min(d, mind)
                        
                self.bitmap.setPixel (ix, iy, colour)

#-----------------------------------------------------------------------
    def drawBands(self,use_r = 1,use_i = 1):
        """
        Draw a mandelbrot based on the current values. Pattern is
        coloured according to the bands colouring scheme, which treets how
        close the iterand gets to the origin in the x and y directions before
        escaping as separate contributions to the final colour.
        'use_i' and 'use_r' can be used to switch off the individual halves
        of the pattern.
        """

        xmin    = self.xpos - self.scale * self.size [0] / 2
        ymin    = self.ypos - self.scale * self.size [1] / 2
        ilist   = range (0, self.iterations)
        ixrange = range (0, self.size [0])
        iyrange = range (0, self.size [1])
        xrange  = [xmin + self.scale * ix for ix in ixrange]
        yrange  = [ymin + self.scale * iy for iy in iyrange]

        z0 = complex (self.z_start [0], self.z_start [1])        

        for ix in ixrange:
            for iy in iyrange:
                c = complex (xrange [ix],yrange [iy])
                z = z0
                colour = BLACK_INDEX
                minx = 2
                miny = 2
                
                for i in ilist:
                    z = z * z + c
                    d = abs (z)
                    
                    if d >= 2:
                        colour = 17
                        if use_r:
                            colour += 16 * min (int (minx/self.starfactor), 14)
                        else:
                            colour += 224
                        if use_i:
                            colour += min (int (miny/self.starfactor), 14)
                        else:
                            colour += 14
                        #n1 = min (int (minx/self.starfactor), 14)+1
                        #n2 = min (int (miny/self.starfactor), 14)+1
                        colour = chr(colour)
                        break
                    else:
                        minx = min(abs(z.real), minx)
                        miny = min(abs(z.imag), miny)
                        
                self.bitmap.setPixel (ix, iy, colour)

#-----------------------------------------------------------------------
    def drawJuliaStars(self):
        """
        Draw a Julia set based on the current values using the star
        colouring algorithm.  Pattern is coloured according to how close
        the iterand gets to the origin before escaping.
        """

        xmin    = self.xpos - self.scale * self.size [0] / 2
        ymin    = self.ypos - self.scale * self.size [1] / 2
        ilist   = range (0, self.iterations)
        ixrange = range (0, self.size [0])
        iyrange = range (0, self.size [1])
        xrange  = [xmin + self.scale * ix for ix in ixrange]
        yrange  = [ymin + self.scale * iy for iy in iyrange]

        c = complex (self.julia_point [0], self.julia_point [1])        
        
        for ix in ixrange:
            for iy in iyrange:
                z = complex (xrange [ix],yrange [iy])
                colour = BLACK_INDEX
                mind = 2
                
                for i in ilist:
                    z = z * z + c
                    d = abs (z)
                    
                    if d >= 2:
                        n = int (mind/self.starfactor)
                        n = min (n, 254)
                        colour = chr(n+1)
                        break
                    else:
                        mind = min(d, mind)
                        
                self.bitmap.setPixel (ix, iy, colour)

#-----------------------------------------------------------------------
    def drawJuliaBands(self,use_r = 1,use_i = 1):
        """
        Draw a Julia set based on the current values using the bands
        colouring algorithm.  Pattern is coloured according to how close
        the iterand gets to the real and imaginary axes before escaping.
        'use_i' and 'use_r' can be used to switch off the individual halves
        of the pattern.
        """

        xmin    = self.xpos - self.scale * self.size [0] / 2
        ymin    = self.ypos - self.scale * self.size [1] / 2
        ilist   = range (0, self.iterations)
        ixrange = range (0, self.size [0])
        iyrange = range (0, self.size [1])
        xrange  = [xmin + self.scale * ix for ix in ixrange]
        yrange  = [ymin + self.scale * iy for iy in iyrange]

        c = complex (self.julia_point [0], self.julia_point [1])        
        
        for ix in ixrange:
            for iy in iyrange:
                z = complex (xrange [ix],yrange [iy])
                colour = BLACK_INDEX
                minx = 2
                miny = 2
                
                for i in ilist:
                    z = z * z + c
                    d = abs (z)
                    if d >= 2:
                        colour = 17
                        if use_r:
                            colour += 16 * min (int (minx/self.starfactor), 14)
                        else:
                            colour += 224
                        if use_i:
                            colour += min (int (miny/self.starfactor), 14)
                        else:
                            colour += 14

                        #n1 = min (int (minx/self.starfactor), 14)+1
                        #n2 = min (int (miny/self.starfactor), 14)+1
                        #colour = chr(16*n1+n2)
                        colour = chr(colour)                            
                        break
                    else:
                        minx = min(abs(z.real), minx)
                        miny = min(abs(z.imag), miny)
                        
                self.bitmap.setPixel (ix, iy, colour)

#-----------------------------------------------------------------------
    def whereIs(self, xpos, ypos):
        """
        Given a co-ordinate in pixel space returns its co-ordinates
        in the complex plane
        """

        x = self.xpos + self.scale * (xpos - self.size [0] / 2)
        y = self.ypos + self.scale * (ypos - self.size [1] / 2)

        return (x,y)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setIterations (self, num):
        """
        Set the number of iteration and the colour map
        """
        
        self.buildColourMap (num)
        self.iterations = num
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def buildColourMap (self, size):
        """
        Build a colour map with the specified number of colours.
        Index 0 relates to black, 1 - 255 are up for grabs.
        """

        add = 255 - (size % 255)
        f   = float (size + add) / float (size)

        self.colour_map = [chr(1 + (int(i * f) % 255)) for i in range (0,size)]

        self.pfuns [self.palette] ()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def pf1 (self):
        """        Creates the palette colours for the bitmap.
        Dark Blue -> Cyan -> Green
        """

        palette = [BLACK]

        m1 = ColourMap.createLinear (ColourMap.dk_blue, ColourMap.cyan, 128)
        m2 = ColourMap.createLinear (ColourMap.cyan, ColourMap.dk_green, 128)

        m1 = m1 [:-1] + m2

        for m in m1:
            m = m + chr(0)
            palette.append (m)

        self.bitmap.colourmap = palette

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def pf2 (self):
        """        Creates the palette colours for the bitmap.
        Dark Red -> Yellow -> Blue
        """

        palette = [BLACK]

        m1 = ColourMap.createLinear (ColourMap.dk_red, ColourMap.yellow, 128)
        m2 = ColourMap.createLinear (ColourMap.dk_blue, ColourMap.cyan, 128)

        m1 = m1 [:-1] + m2

        for m in m1:
            m = m + chr(0)
            palette.append (m)

        self.bitmap.colourmap = palette        
                
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def pf3 (self):
        """        Creates the palette colours for the bitmap.
        Dark blue to cyan. Used for the star drawing algorithm
        """

        palette = [BLACK]

        m1 = ColourMap.createLinear (ColourMap.cyan, ColourMap.dk_blue, 255)

        for m in m1:
            m = m + chr(0)
            palette.append (m)

        self.bitmap.colourmap = palette        

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def pf4 (self):
        """        Creates the palette colours for the bitmap.
        This one increments red and green in 15 steps and is used by the 'bands'
        colouring scheme.
        """

        palette = [BLACK]*256

        for i in range (0,15):
            green = 255-16*i
            for j in range (0,15):
                red = 255-12*j
                idx = 16*i+j+17
                palette[idx]=chr(0)+chr(green)+chr(red)+chr(0)

        self.bitmap.colourmap = palette        

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def pf5 (self):
        """        Creates the palette colours for the bitmap.
        This one increments blue and green in 15 steps and is used by the 'bands'
        colouring scheme.
        """

        palette = [BLACK]*256

        for i in range (0,15):
            green = 255-16*i
            for j in range (0,15):
                blue = 255-12*j
                idx = 16*i+j+17
                palette[idx]=chr(blue)+chr(green)+chr(0)+chr(0)

        self.bitmap.colourmap = palette        
