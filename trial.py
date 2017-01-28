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

import urllib2, httplib
httplib.HTTPConnection.debuglevel = 1
request = urllib2.Request('http://ow.ly/gxoS308a1EM')
opener = urllib2.build_opener()
f=opener.open(request)
print f.url