from mnist import MNIST
import numpy as np
from sklearn.neighbors import  KNeighborsClassifier

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

print "Holololol 3n Uniform p=1"
del train_raw
del mn
del test_raw

nbrsModel = KNeighborsClassifier(\
	n_neighbors=3,\
	weights = 'uniform',\
	algorithm = 'auto',\
	metric = 'minkowski',\
	p=1,\
	n_jobs = -1)
print "POP"
nbrsModel.fit(train_data,train_labels)
print "POOP"
print(nbrsModel.score(test_data,test_labels))