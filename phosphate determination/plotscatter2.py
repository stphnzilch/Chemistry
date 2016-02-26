import pylab
from pylab import *
import matplotlib.pyplot as plt

from scipy import stats
import numpy as np
from matplotlib.legend_handler import HandlerLine2D

x=[0, 0.08, 0.4, 0.8, 2, 10, ]
y=[0.002, -0.054, 0.02, 0.086, 0.454, 2.336, ]
MGx = [1.849041533]
MGy =  [0.403]
RFx = [-0.2915335463]
RFy  = [-0.133]
scatter(MGx,MGy, label='Miracle Gro 1:100', marker='o', color='r')
scatter(RFx,RFy, label='Rainbow Falls',marker='o', color='g')
(m,b)=polyfit(x,y,1)
yp = polyval([m,b],x)
plot(x,yp)
scatter(x,y, label='standard')
grid(True)
xlabel('ppM')
ylabel('Abs')
title('Calibration Curve Phosphate with Samples')
text(0, 2, r'y=0.23x-0.06')
text(0, 1.8, r'r-squared: 0.998')
legend(loc=4)
show()
