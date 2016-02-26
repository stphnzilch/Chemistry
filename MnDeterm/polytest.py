from numpy import *
from matplotlib.pyplot import *

x = [0, .08, .4, 2, 10, 100]
y = [-0.0002,	0.006,	0.0314,	0.1588,	0.7928,	1.6744] #std


coefficients = polyfit(x, y, 6)
polynomial = poly1d(coefficients)
xs = x
ys = y

plot(x, y, 'o')
plot(xs, ys)
ylabel('y')
xlabel('x')
show()
