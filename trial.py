# #!/usr/bin/env python
# from contextlib import closing
# from selenium.webdriver import Firefox # pip install selenium
# from selenium.webdriver.support.ui import WebDriverWait
#
# url='www.facebook.com'
#
# # use firefox to get page with javascript generated content
# with closing(Firefox()) as browser:
#     browser.get(url)
#     button = browser.find_element_by_name('button')
#     button.click()
#     # wait for the page to load
#     WebDriverWait(browser, timeout=10).until(
#         lambda x: x.find_element_by_id('loginbutton'))
#     # store it to string variable
#     page_source = browser.page_source
# print(page_source)


# import dryscrape
# from bs4 import BeautifulSoup
# session = dryscrape.Session()
# session.visit('https://www.quora.com/How-can-I-get-the-HTML-CSS-JavaScript-source-code-of-a-website')
# response = session.body()
# soup = BeautifulSoup(response,"lxml")
# print soup.find(id="async_spinner")
# import urllib2, httplib
# httplib.HTTPConnection.debuglevel = 1
# request = urllib2.Request('http://ow.ly/gxoS308a1EM')
# opener = urllib2.build_opener()
# f=opener.open(request)
# print f.url

# from selenium import webdriver
#
# browser = webdriver.Firefox()
# browser.get('http://seleniumhq.org/')

#from selenium import webdriver
#url = 'http://www.stackoverflow.com'
#driver = webdriver.PhantomJS()
#driver.get(url)
#print driver.page_source

# import whois
# from datetime import datetime
# import time
# try:
#     domain=whois.query("dbfjefklj.com")
# except:
#     print -1
# creation_date=domain.creation_date
# expiration_date=domain.expiration_date
# #creation_date=datetime.strptime(creation_date,"%Y-%m-%d")
# #expiration_date=datetime.strptime(expiration_date,"%Y-%m-%d")
# #today=datetime.datetime.today().strftime('%Y-%m-%d')
# today=time.strftime('%Y-%m-%d')
# today=datetime.strptime(today,'%Y-%m-%d')
# ageofdomain=abs((expiration_date - creation_date).days)
# if ageofdomain/30<6:
#     print -1
# else:
#     print 1
#
# registration_length=abs((expiration_date-today).days)
#
# if registration_length/365<=1:
#     print -1
# else:
#     print 1
# print registration_length
# print ageofdomain
# print creation_date
# print expiration_date

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

import features_extraction

labels=[]
features=[]
file=open('/home/rohit/PycharmProjects/BE/Training.arff').read()
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

# features_train=features[:10000]
# labels_train=labels[:10000]
##### Features_train doesn't have to be different from features anymore since all the features will be used for training #####
# features_test=features[10000:]
# labels_test=labels[10000:]
features_test=features_extraction.status

print(" ""Support Vector Machine Results"" ")
clf1 = svm.SVC(kernel="rbf",C=10000.0,gamma=0.1,probability=True)
# clf1.fit(features_train,labels_train)
clf1.fit(features, labels)
pred1=clf1.predict(features_test)
#print(classification_report(labels_test, pred1))
# print 'The accuracy is:', accuracy_score(labels_test, pred1)
print 'The predicted label is ', pred1

print("\n\n ""Naive Bayes Algorithm Results"" ")
clf2 = GaussianNB()
# clf2.fit(features_train, labels_train)
clf2.fit(features, labels)
pred2=clf2.predict(features_test)
#print(classification_report(labels_test, pred2))
# print 'The accuracy is:', accuracy_score(labels_test, pred2)
print 'The predicted label is ', pred2

print("\n\n ""K-Nearest Neighbours Algorithm Results"" ")
clf3 = KNeighborsClassifier()
# clf3.fit(features_train, labels_train)
clf3.fit(features, labels)
pred3=clf3.predict(features_test)
#print(classification_report(labels_test, pred3))
# print 'The accuracy is:', accuracy_score(labels_test, pred3)
print 'The predicted label is ', pred3

print("\n\n ""Random Forest Algorithm Results"" ")
clf4 = RandomForestClassifier( min_samples_split=3)
# clf4.fit(features_train, labels_train)
clf4.fit(features, labels)
pred4=clf4.predict(features_test)
#print(classification_report(labels_test, pred4))
# print 'The accuracy is:', accuracy_score(labels_test, pred4)
print 'The predicted label is ', pred4