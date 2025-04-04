# -*- coding: utf-8 -*-
"""Bagging.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ci-OriUBV7S-sTMkdBxEhCyOLueM_CZv
"""

from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.metrics import accuracy_score
import numpy as np


dataset = datasets.load_breast_cancer()

X = dataset.data
Y = dataset.target

target_names = dataset.target_names
feature_names = dataset.feature_names

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)



from sklearn.ensemble import BaggingClassifier
clf = BaggingClassifier(estimator=tree.DecisionTreeClassifier(), n_estimators=10, random_state=0)
clf.fit(X_train, Y_train)


predictedY_test = clf.predict(X_test)
predictedY_train = clf.predict(X_train)

accuracy_train = accuracy_score(Y_train, predictedY_train)
accuracy_test = accuracy_score(Y_test, predictedY_test)

print("Accuracy for train set: %f" %(accuracy_train*100))
print("Accuracy for test set: %f" %(accuracy_test*100))