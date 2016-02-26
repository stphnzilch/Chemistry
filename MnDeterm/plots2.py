from numpy import *

from matplotlib.pyplot import *
x  = linspace(-2, 2, 100)

figure()

subplot(2,2,1)   # Two rows and two cols of plots, select first one

plot(x, x)

subplot(2,2,2)   # Two rows and two cols of plots, select second one

plot(x, x**2)

subplot(2,2,3)   # Two rows and two cols of plots, select third one

plot(x, x**3)

subplot(2,2,4)   # Two rows and two cols of plots, select fourth one

plot(x, x**4)

savefig("plot_subplots.png")
