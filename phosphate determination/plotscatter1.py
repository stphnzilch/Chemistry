import pylab
from pylab import *
import matplotlib.pyplot as plt

from scipy import stats
import numpy as np

x=[0, 0.08, 0.4, 0.8, 2, 10]
y=[0.002, -0.054, 0.02, 0.086, 0.454, 2.336]


(m,b)=polyfit(x,y,1)
print b 
print m
yp = polyval([m,b],x)
slope= "y=", m, "x+", b
print "slope: ", slope
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print "r-squared:", r_value**2
plot(x,yp)
scatter(x,y)
grid(True)
xlabel('ppM')
ylabel('Abs')
title('Calibration Curve Phosphate')
text(0, 2, r'y=0.23x-0.06')
text(0, 1.8, r'r-squared: 0.998')

show()
#fig = plt.figure()

#ax1 = fig.add_subplot(111)


#ax1.set_title("Plot title...")    
#ax1.set_xlabel('your x label..')
#ax1.set_ylabel('your y label...')


#pylab.plot(x,y,'co')





pylab.show()


