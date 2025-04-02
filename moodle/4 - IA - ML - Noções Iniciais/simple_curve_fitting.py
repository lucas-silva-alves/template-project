import matplotlib.pyplot as plt
import numpy as np
#import ipdb

x = np.linspace(-10, 10, 21)
y = x+2*np.sin(x)


z = np.polyfit(x, y, 13)  #polynomial coefficients
#z = np.polyfit(x, y, 3)  #polynomial coefficients
p = np.poly1d(z)          #prediction function based on polynomial coefficients

xp = np.linspace(-15, 15, 100)
ycontinued = xp+2*np.sin(xp)  # original function continued beyond fitting data

plt.plot(x, y, 'bo', label='data used for fitting')
plt.plot(xp, ycontinued, 'g--', label='data beyond used for fitting')
plt.plot(xp, p(xp), 'r-', label='best fit')
plt.legend(loc='best')

plt.ylim((min(ycontinued)-1,max(ycontinued)+1))
plt.show()
