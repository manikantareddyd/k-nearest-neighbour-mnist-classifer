from mnist import MNIST
import numpy as np
from sklearn.neighbors import  KNeighborsClassifier
from sklearn.metrics import *
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

print "*"*60
del train_raw
del mn
del test_raw
print 'Number of Neighbours:',sys.argv[1]
if int(sys.argv[2])==1:
	Weights='uniform'
	print "Using Uniform Weights"
else:
	Weights='distance'
	print "Using Inverse Distance Weights"

print "Using p =",sys.argv[3]," in minkowski distance metric"
nbrsModel = KNeighborsClassifier(\
	n_neighbors=int(sys.argv[1]),\
	weights = Weights,\
	algorithm = 'auto',\
	metric = 'minkowski',\
	p=int(sys.argv[3]),\
	n_jobs = 3)


nbrsModel.fit(train_data,train_labels)
print "\n"
print "Confusion Matrix"
predicted_labels = nbrsModel.predict(test_data)
del train_data
del test_data
print confusion_matrix(test_labels,predicted_labels,labels=[0,1,2,3,4,5,6,7,8,9])
hits=0
for i in range(0,10000):
	if predicted_labels[i]==test_labels[i]:
		hits=hits+1

print "\n"
print "Classification Report"
print classification_report(test_labels,predicted_labels,target_names=['0','1','2','3','4','5','6','7','8','9'])
print "\n"
print "Accuracy=",hits/10000.0
print "*"*60,"\n"
#print nbrsModel.score(test_data,test_labels), int(sys.argv[1]), Weights, sys.argv[3]
