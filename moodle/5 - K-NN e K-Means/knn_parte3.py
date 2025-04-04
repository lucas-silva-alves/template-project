# -*- coding: utf-8 -*-
"""KNN_parte3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NfjnYrs_0LHqcTtpBeyBOBZ7hsI2K8eo

# KNN - Parte 3 (teste simplificado com base *breast cancer*)
"""

from sklearn import neighbors
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
# import ipdb

dataset = datasets.load_breast_cancer()

X = dataset.data[:, :2]
Y = dataset.target

clf = neighbors.KNeighborsClassifier(n_neighbors=13)

clf = clf.fit(X, Y)

print(clf.predict([[0.9, 1.1]]))


#ipdb.set_trace()


#****************
# Plot
# baseado em https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html
#****************
step_size = 0.1
# encontrando os limites
x_min, x_max = X[:, 0].min(), X[:, 0].max()
y_min, y_max = X[:, 1].min(), X[:, 1].max()

x_min, x_max = x_min-abs(0.1*x_min), x_max+abs(0.1*x_max)
y_min, y_max = y_min-abs(0.1*y_min), y_max+abs(0.1*y_max)


xx, yy = np.meshgrid(np.arange(x_min, x_max, step_size), np.arange(y_min, y_max, step_size))

Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

Z = Z.reshape(xx.shape)

plt.figure()
plt.pcolormesh(xx, yy, Z, cmap='Set3')

# plot training points
plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolor='k', s=20, cmap='Set3')

plt.show()

np.max(dataset.data[:,0])

dataset