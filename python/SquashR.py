""""SqaushR Core V 1.0"""
import os
from os.path import splitext
import sklearn 
from sklearn import datasets
print("Hello SqaushR")
iris = datasets.load_iris()
print(iris.data)


def splitext_(path):
    if len(path.split('.')) > 2:
        return path.split('.')[0], '.'.join(path.split('.')[-2:])
    return splitext(path)
