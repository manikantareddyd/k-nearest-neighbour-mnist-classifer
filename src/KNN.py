from mnist import MNIST
import numpy as np
from sklearn.neighbors import  KNeighborsClassifier
import sys

mn  = MNIST('./data')
train_raw = mn.load_training()
test_raw = mn.load_testing()

train_labels = []
train_data = []
test_labels = []
test_data=[]
for i in range(0,60000):
	train_labels.append(train_raw[1][i])
	train_data.append(train_raw[0][i])
for i in range(0,10000):
	test_labels.append(test_raw[1][i])
	test_data.append(test_raw[0][i])


del train_raw
del mn
del test_raw
if int(sys.argv[2])==1:
	Weights='uniform'
else:
	Weights='distance'

nbrsModel = KNeighborsClassifier(\
	n_neighbors=int(sys.argv[1]),\
	weights = Weights,\
	algorithm = 'auto',\
	metric = 'minkowski',\
	p=sys.argv[3],\
	n_jobs = -1)

nbrsModel.fit(train_data,train_labels)

print nbrsModel.score(test_data,test_labels), int(sys.argv[1]), Weights, sys.argv[3]