from numpy import *

from matplotlib.pyplot import *
x  = linspace(-2, 2, 100)

figure()

   # Two rows and two cols of plots, select first one

plot(2*x, 2*x)

   # Two rows and two cols of plots, select second one

plot(2*x, 2*x**2,2)



show()
