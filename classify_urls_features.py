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
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix
from sklearn import preprocessing
from sklearn import metrics


import sys
import joblib

labels=[]
features=[]
file=open('/home/janvi-jatakia/PycharmProjects/BE/Training Dataset.arff').read()
list=file.split('\r\n')
#f=open('/home/janvi-jatakia/Downloads/data.txt','w')
data=np.array(list)
data1=[i.split(',') for i in data]
data1=data1[0:-1]
for i in data1:
	labels.append(i[30])
data1=np.array(data1)
features=data1[:,:-1]
features=features[:,[0,1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,22,23,24,25,27,29]]
#print features
features=np.array(features).astype(np.float)

features_train=features[:10000]
labels_train=labels[:10000]
features_test=features[10000:]
labels_test=labels[10000:]

print(" ""Support Vector Machine Results"" ")
clf1 = svm.SVC(probability=True)
clf1.fit(features_train,labels_train)
pred1=clf1.predict(features_test)
print(classification_report(labels_test, pred1))
print 'The accuracy is:', accuracy_score(labels_test, pred1)
print metrics.confusion_matrix(labels_test, pred1)
#
# lb = preprocessing.LabelBinarizer()
# lb.fit(features_train)
# print(recall_score(labels_test, pred1 ,None))


# print("\n\n ""Naive Bayes Algorithm Results"" ")
# clf2 = GaussianNB()
# clf2.fit(features_train, labels_train)
# pred2=clf2.predict(features_test)
# print(classification_report(labels_test, pred2))
# print 'The accuracy is:', accuracy_score(labels_test, pred2)
# print metrics.confusion_matrix(labels_test, pred2)


print("\n\n ""K-Nearest Neighbours Algorithm Results"" ")
clf3 = KNeighborsClassifier()
clf3.fit(features_train, labels_train)
pred3=clf3.predict(features_test)
print(classification_report(labels_test, pred3))
print 'The accuracy is:', accuracy_score(labels_test, pred3)
print metrics.confusion_matrix(labels_test, pred3)

print("\n\n ""Random Forest Algorithm Results"" ")
clf4 = RandomForestClassifier(min_samples_split=7)
clf4.fit(features_train, labels_train)
pred4=clf4.predict(features_test)
print(classification_report(labels_test, pred4))
print 'The accuracy is:', accuracy_score(labels_test, pred4)
print metrics.confusion_matrix(labels_test, pred4)

sys.setrecursionlimit(9999999)
joblib.dump(clf4, 'classifier/random_forest.pkl',compress=9)

