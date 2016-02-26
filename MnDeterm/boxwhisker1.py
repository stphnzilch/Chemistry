## numpy is used for creating fake data
import numpy as np 
import matplotlib as mpl 

## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt 

collectn_1 =  [-0.001, 0, 0, 0, 0]
collectn_2 = [0.006,0.006, 0.006, 0.006, 0.006]
collectn_3 = [0.031, 0.031, 0.031, 0.032, 0.032]
collectn_4 = [0.16, 0.16, .158, .158, .158]

data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot)

# Save the figure
fig.savefig('fig1.png', bbox_inches='tight')
