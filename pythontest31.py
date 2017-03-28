import fractals

f = fractals.Mandelbrot("myfractal.png",(640,480),n=128,box=((.34,.57),(.34+.036,.57+.027)))
f.compute()

