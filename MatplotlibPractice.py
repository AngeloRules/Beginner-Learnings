import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,11,10)
y = x*2
# fig = plt.figure() # takes additional arguments such as 'figsize' = (length,height), 'dpi' = ()
# axes1 = plt.axes([0.05,0.01,0.8,0.8])
# axes2 = fig.add_axes([0.5,0.2,0.4,0.4])
# axes1.set_xlabel('X LABEL')
# axes1.set_ylabel('Y LABEL')
# axes1.set_title('FIRST PLOT')
# axes1.plot(x,np.log(y), color='red')
# axes2.plot(x,y)
# plt.show()

fig,axes = plt.subplots(nrows=1, ncols=2) #axes is actually an array of objects, therefore they can be indexed
axes[1].plot(x,y, color='purple')
# .plot() takes a number of arguments such as

# color - allows us to choose a color for the line color
# linewidth(lw) = allows us to set a size for the line
# alpha - allows us to select the transperency of the plot line
#linestyle(ls) - allows us to choose a linestyle(dotted,dashed,etc)
# markers - allows us to select a marker for the data points
# markersize - allows us to change the size of the marker
# additional arguments include, markerfacecolor, markeredgewidth,markeredgewidth
plt.tight_layout()
plt.show()
