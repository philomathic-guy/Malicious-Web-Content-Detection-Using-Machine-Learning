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
#river.get(url)
#print driver.page_source
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
file=open('/home/anand/PycharmProjects/BE/Training Dataset.arff').read()
list=file.split('\r\n')
#f=open('/home/janvi-jatakia/Downloads/data.txt','w')
data=np.array(list)
print "yaha"
print data
data1=[i.split(',') for i in data]
data1=data1[0:-1]
for i in data1:
	labels.append(i[30])
data1=np.array(data1)
features=data1[:,:-1]
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
