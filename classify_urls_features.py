import numpy as np
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

labels=[]
features=[]
file=open('/home/janvi-jatakia/Downloads/Training.arff').read()
list=file.split('\r\n')
#f=open('/home/janvi-jatakia/Downloads/data.txt','w')
data=np.array(list)
data1=[i.split(',') for i in data]
data1=data1[0:-1]
for i in data1:
	labels.append(i[30])
data1=np.array(data1)
features=data1[:,:-1]
features=features[:,[0,1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,18,19,20,21,22,25,26,27]]
#print features
features=np.array(features).astype(np.float)

features_train=features[:10000]
labels_train=labels[:10000]
features_test=features[10000:]
labels_test=labels[10000:]

print(" ""Support Vector Machine Results"" ")
clf1 = svm.SVC(kernel="rbf",C=10000.0,gamma=0.1,probability=True)
clf1.fit(features_train,labels_train)
pred1=clf1.predict(features_test)
#print(classification_report(labels_test, pred1))
print 'The accuracy is:', accuracy_score(labels_test, pred1)

print("\n\n ""Naive Bayes Algorithm Results"" ")
clf2 = GaussianNB()
clf2.fit(features_train, labels_train)
pred2=clf2.predict(features_test)
#print(classification_report(labels_test, pred2))
print 'The accuracy is:', accuracy_score(labels_test, pred2)

print("\n\n ""K-Nearest Neighbours Algorithm Results"" ")
clf3 = KNeighborsClassifier()
clf3.fit(features_train, labels_train)
pred3=clf3.predict(features_test)
#print(classification_report(labels_test, pred3))
print 'The accuracy is:', accuracy_score(labels_test, pred3)

print("\n\n ""Random Forest Algorithm Results"" ")
clf4 = RandomForestClassifier( min_samples_split=3)
clf4.fit(features_train, labels_train)
pred4=clf4.predict(features_test)
#print(classification_report(labels_test, pred4))
print 'The accuracy is:', accuracy_score(labels_test, pred4)
