import matplotlib.pyplot as plt
import numpy as np
#import ipdb
#import sklearn
from sklearn.model_selection import train_test_split

X_total = np.linspace(-15, 15, 100)
y_total = X_total+2*np.sin(X_total)

X_train, X_test, y_train, y_test = train_test_split(X_total,y_total, test_size=0.33, random_state=3)
#ipdb.set_trace()
#z = np.polyfit(x, y, 13)  #polynomial coefficients
z = np.polyfit(X_train, y_train, 13)  #polynomial coefficients
p = np.poly1d(z)          #prediction function based on polynomial np.linspace no help forcoefficients

#xp = np.linspace(-15, 15, 100)
y_continued = p(X_total)  # original function continued beyond fitting data

plt.plot(X_train, y_train, 'bo', label='data used for fitting')
plt.plot(X_total, y_total, 'g--', label='total data')
plt.plot(X_total, y_continued, 'r-', label='best fit')
plt.legend(loc='best')


plt.ylim((min(y_continued)-1,max(y_continued)+1))
plt.show()
