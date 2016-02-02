from mnist import MNIST
import numpy as np
from sklearn.neighbors import  KNeighborsClassifier
import sys

mn  = MNIST('./data')
train_raw = mn.load_training()
test_raw = mn.load_testing()