#==============================================================
# (c) John Whitehouse 2002-2003
# htpp://www.eddaardvark.co.uk/
#
# Command line interface module to drive the mandelbror drawer
#==============================================================

import Mandelbrot.py
import string
import sys
import os

# Default settings

class Settings:
    """
        Collect all the settings into an object
    """

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self):
        """
            initialise the key handler map and set the default values
        """

        self.keyhandlers = {
            'a':self.setActivePoint,
            'b':self.setStarFactor,
            'c':self.setCValue,
            'd':self.setColourScheme,
            'f':self.setFileName,
            'h':self.showHelp,
            'i':self.setIterations,
            'm':self.setMagnification,
            'n':self.setNoDraw,
            'p':self.setPath,
            's':self.setSize,
            't':self.setType,
            'w':self.setWhereIs,
            'z':self.setJuliaOrigin,
        }

    # default values

        self.type = 'Mandelbrot'     # Mandelbrot
        self.sub_type = 'Normal'     # Normal colouring scheme
        self.filename = "mandelbrot" # The file name to save the pattern as
        self.path = "c:\\"           # The path to save data files
        self.j_origin = (0,0)        # The drawing centre (for Julia Sets)
        self.c_value = None          # the 'c' value in the equation (drawing center for Mandelbrot)
        self.magnify = 1             # Magnification (>1 to zoom in)
        self.active_point = 0        # The active point
        self.iterations = 600        # The number of iterations
        self.size = (160, 120)       # The size in pixels of the image to draw
        self.draw_it = 1             # Draw the pattern
        self.show_help = 0           # Should we show the help
        self.where_is = None         # 'Where is' point
        self.palette = None          # 1st colour scheme
        self.starfactor = 0.001 ;    # Star factor in star colouring scheme
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doHelp(self):
        "Show the help"
        
        print "Parameters..."
        print "  -a<number> - Sets the 'c' value to one of the predefined active points"
        print "  -b<number> - Blob factor, controls the star size with star colouring"
        print "  -c(x,y)    - The 'C' value for Julia Sets, image centre for Mandelbrots"
        print "  -d<number> - Drawing colour scheme to use (1-3)"
        print "  -f<name>   - Output file name, without path or extension"
        print "  -h         - Shows this help"
        print "  -i<number> - Set the maximum number of iterations"
        print "  -m<number> - Magnification - 1 = whole picture, >1 zooms in"
        print "  -n         - NoDraw - just prints the parameters"
        print "  -p<path>   - Sets the path"
        print "  -s<w>x<h>  - Sets the size of the pattern to draw"
        print "  -t<type>   - The type & sub-type of pattern"
        print "                 M  - Mandelbrot set, normal colouring"
        print "                 J  - Julia Set, normal colouring"
        print "                 MS/JS - with star colouring"
        print "                 MB/JB - with banded colouring"
        print "                 MR/JR - With the real axis subset of bands"
        print "                 MI/JI - With the imaginary axis subset of bands"
        print "  -w(x,y)    - Returns the position of the pixel at (x,y). No Drawing"
        print "  -z(x,y)    - The drawing centre for Julia Sets, Z0 for Mandelbrots"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def showHelp (self, dummystr):
        """
        Show some help
        """

        self.show_help = 1
        self.draw_it = 0

        return 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setNoDraw (self, dummystr):
        """
        Turn of the actual drawing - used to test parameter parsing
        """

        self.draw_it = 0

        return 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def go(self):
        """
        Apply the parameters and draw the picture (or show the help)
        """
        
# If help requested then go no further

        if self.show_help:
            self.doHelp ()

        else:
            self.applyParameters()
            if self.draw_it:
                self.draw()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def applyParameters(self):
        """
        Make any required adjustments to the parameters
        """

    # Fix up unset parameters - 'c' value (both)

        if self.c_value == None:
            self.c_value = Mandelbrot.interesting_coords [self.active_point]

    # Choose the default colour scheme if it hasn't been set

        palette_map = {
        'Standard':1,
        'Stars':3,
        'Bands':4,
        'Real Bands':4,
        'Imaginary Bands':4,
        }

        if self.palette  == None:
            self.palette = palette_map [self.sub_type]

    # Print out what we've chosen

        print "  Pattern type:  ", self.type, ", scheme = ", self.sub_type
        print "  Size:          ", self.size [0], "x", self.size [1]
        print "  File name:     ", self.path + self.filename + '.bmp'
        print "  Julia Origin:  ", self.j_origin
        print "  C Value:       ", self.c_value
        print "  Where is:      ", self.where_is
        print "  Magnification: ", self.magnify
        print "  Iterations:    ", self.iterations
        print "  Colour Scheme: ", self.palette
        print "  Star Factor:   ", self.starfactor

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def draw(self):
        """
        Draw a pattern based on the settings
        """

        # Initialise the pattern

        m = Mandelbrot.Mandelbrot ()

        if self.type == 'Mandelbrot':
            m.z_start = self.j_origin
            m.xpos    = self.c_value [0]
            m.ypos    = self.c_value [1]
            m.scale   = 4.0/(self.magnify * self.size[0])

        else:
            m.julia_point = self.c_value
            m.xpos = self.j_origin [0]
            m.ypos = self.j_origin [1]
            m.scale = 4.0/(self.magnify * self.size[0])

    # Draw the appropriate pattern type        

        m.palette = self.palette - 1
        m.starfactor = self.starfactor
        
        m.setSize       (self.size)
        m.setIterations (self.iterations)

        if self.where_is == None:
            if self.type == 'Mandelbrot':
                if self.sub_type == 'Standard':
                    m.draw = m.drawStandard ()
                elif self.sub_type == 'Stars':
                    m.draw = m.drawStars ()
                elif self.sub_type == 'Bands':
                    m.draw = m.drawBands ()
                elif self.sub_type == 'Real Bands':
                    m.draw = m.drawBands (1,0)
                elif self.sub_type == 'Imaginary Bands':
                    m.draw = m.drawBands (0,1)
            elif self.type == 'Julia Set':
                if self.sub_type == 'Standard':
                    m.draw = m.drawJulia ()
                elif self.sub_type == 'Stars':
                    m.draw = m.drawJuliaStars ()
                elif self.sub_type == 'Bands':
                    m.draw = m.drawJuliaBands ()
                elif self.sub_type == 'Real Bands':
                    m.draw = m.drawJuliaBands (1,0)
                elif self.sub_type == 'Imaginary Bands':
                    m.draw = m.drawJuliaBands (0,1)
            
        # Write out the bitmap

            file = self.path + self.filename + '.bmp'
            m.bitmap.writeFile(file)

    # Print the whereis value (screen co-ords are upside down)
    
        else:
            x = self.where_is [0]
            y = self.size [1] - self.where_is [1]

            where = m.whereIs (x, y)                
            
            print "(%f, %f) is at (%12.10f, %12.10f)" % (self.where_is [0], self.where_is [1], where [0], where [1])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def process (self, arg):
        """
        Process a command string. All command strings have the format
        "-<letter><string>" or "/<letter><string>"
        <string. can't contain spaces.
        """
        if len(arg)>1 and (arg[0]== '-' or arg[0]=='/'):
            try:
                return self.keyhandlers[arg[1]](arg[2:])
            except KeyError:
                print "  Unknown parameter:", arg

        return 0                
                
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setType (self, typestr):
        """
        Decode the pattern type string '-tPattern', The first letter can be
            J       Julia Set
            M       Standard Mandelbrot set

        The second letter can be
            (none)  Normal colouring scheme
            S       Use the stars colouring scheme
            B       Use the bands colouring scheme
        """

        valid_types = {
        'M':('Mandelbrot','Standard'),
        'MS':('Mandelbrot','Stars'),
        'MB':('Mandelbrot','Bands'),
        'MR':('Mandelbrot','Real Bands'),
        'MI':('Mandelbrot','Imaginary Bands'),
        'J':('Julia Set','Standard'),
        'JS':('Julia Set','Stars'),
        'JB':('Julia Set','Bands'),
        'JR':('Julia Set','Real Bands'),
        'JI':('Julia Set','Imaginary Bands'),
        }

        try:
            t = valid_types [typestr]
            self.type     = t[0]
            self.sub_type = t[1]
            
        except KeyError:
            print "  '%s' is not a valid pattern type" % (typestr)
            return 0
            
        return 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setFileName (self, fnstr):
        """
        Set the file name. Strip off any extension. We'll add
        a '.bmp' later.
        """

        if len (fnstr) > 0:
            self.filename = fnstr
            dotpos = string.rfind (self.filename, '.')
            if dotpos >= 0:
                self.filename = self.filename [:dotpos]
            
        return 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setPath (self, pathstr):
        """
        Set the output path
        """

        if len (pathstr) > 0:
            if pathstr [-1] != '\\':
                pathstr += '\\'
                
            self.path = os.path.abspath(pathstr) + '\\'
            return 1

        print "  Empty path parameter"
        return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setActivePoint (self, ptstr):
        """
        Sets the active point
        """

        try:
            self.active_point = int (ptstr)
            return 1
        except ValueError:
            pass

        return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setIterations(self, ptstr):
        """
        Sets the number of iterations
        """

        try:
            self.iterations = int (ptstr)
            return 1
        except ValueError:
            pass

        return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setMagnification (self, magstr):
        """
        Set the magnification (1 will draw the whole image, larger
        values zoom in)
        """

        try:
            self.magnify = float (magstr)
            return 1
        except ValueError:
            print "magnification '%s' must be a number" % (magstr)

        return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setStarFactor (self, sfstr):
        """
        Set the star factor - for star patterns
        """

        try:
            self.starfactor = float (sfstr)
            return 1
        except ValueError:
            print "'Star Factor' must be a number" % (sfstr)

        return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setJuliaOrigin (self, posstr):
        """
        Set the origin for Julia Sets.
        Expects a string in the format "(x,y)"
        """

        pos = self.decodeCoord (posstr)

        if pos != None:
            self.j_origin = pos
            return 1
        
        return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setWhereIs (self, posstr):
        """
        Set the 'where is' point. If this is set then rather than draw a
        picture the driver returns the location of the selected pixel
        in 'z' or 'c' space.
        """

        pos = self.decodeCoord (posstr)

        if pos != None:
            self.where_is = pos
            return 1
        
        return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setCValue (self, posstr):
        """
        Set the c value.
        Expects a string in the format "(x,y)"
        """

        pos = self.decodeCoord (posstr)

        if pos != None:
            self.c_value = pos
            return 1
        
        return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setSize (self, sizestr):
        """
        Parse a string of the format "<w>x<h>" into a size
        """

        str = string.strip (sizestr)
        bits = string.split (str, 'x')

        if len(bits) == 2:
            self.size = (int (bits [0]), int (bits [1]))
            return 1

        return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setColourScheme (self, csstr):
        """
        Parse anumber to a colour scheme
        """

        try:
            self.palette = int (csstr)
            return 1
        except ValueError:
            pass

        return 0


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def decodeCoord (self, posstr):
        """
        Parse a string of the format "(x,y)" and return the tuple
        (x,y)
        """

        str = string.strip (posstr)     # remove whitespace
        str = str [1:-1]                # remove '(' and ')'
        bits = string.split (str, ',')

        if len(bits) == 2:
            return (float (bits [0]), float (bits [1]))

        return None

#==============================================================================
# A module level function that allows us to call the example function from
# the command line
#==============================================================================

def go (args):

    ok = 1
    settings = Settings()
    strtype = type ('xxx')
    listtype = type (range (2))

# Output file path
    
    path = os.path.dirname(sys.argv[0])
    settings.path = os.path.abspath(path) + '\\'
    
    print "Mandelbrot Driver..."

    if type(args) != listtype:
        if type(args) == strtype:
            args = string.split (args, ' ')
        else:
            args = ['-h']

# Process the arguments

    for arg in args:
        if ok:
            ok = settings.process (arg)
            if not ok:
                print "Unknown parameter: '%s'" % (arg)

# Draw the picture (or something)

    if ok:
        settings.go()
        
#======================================================================
# Call the entry point
#======================================================================

if len (sys.argv) > 1:
    go (sys.argv[1:]) # skip the program name
else:
    print "Mandelbrot Driver Loaded"
