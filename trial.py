# # #!/usr/bin/env python
# # from contextlib import closing
# # from selenium.webdriver import Firefox # pip install selenium
# # from selenium.webdriver.support.ui import WebDriverWait
# #
# # url='www.facebook.com'
# #
# # # use firefox to get page with javascript generated content
# # with closing(Firefox()) as browser:
# #     browser.get(url)
# #     button = browser.find_element_by_name('button')
# #     button.click()
# #     # wait for the page to load
# #     WebDriverWait(browser, timeout=10).until(
# #         lambda x: x.find_element_by_id('loginbutton'))
# #     # store it to string variable
# #     page_source = browser.page_source
# # print(page_source)
#
#
# # import dryscrape
# # from bs4 import BeautifulSoup
# # session = dryscrape.Session()
# # session.visit('https://www.quora.com/How-can-I-get-the-HTML-CSS-JavaScript-source-code-of-a-website')
# # response = session.body()
# # soup = BeautifulSoup(response,"lxml")
# # print soup.find(id="async_spinner")
# # import urllib2, httplib
# # httplib.HTTPConnection.debuglevel = 1
# # request = urllib2.Request('http://ow.ly/gxoS308a1EM')
# # opener = urllib2.build_opener()
# # f=opener.open(request)
# # print f.url
#
# # from selenium import webdriver
# #
# # browser = webdriver.Firefox()
# # browser.get('http://seleniumhq.org/')
#
# #from selenium import webdriver
# #url = 'http://www.stackoverflow.com'
# #driver = webdriver.PhantomJS()
# #driver.get(url)
# #print driver.page_source
#
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


# import datetime, urllib2, re
#
# url = 'http://google.com/search?'  # Set web search URL
# hits = {'link': 'http://www.spit.ac.in'}
#
# # Generate web search term
# hits['web search term'] = urllib2.quote('link:' + hits['link'])
#
# # Execute web search
# urlstr = '%sq=%s' % (url, hits['web search term'])
# url = urllib2.Request(urlstr)
# url.add_header('User-Agent', '')
# url = urllib2.urlopen(url).read()
#
# # Store date and time of web search
# hits['datetimeutc'] = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
#
# # Parse web search results to determine hits
# hits['hits'] = re.search('Results <b>1</b> - <b>10</b> of about <b>(?P<hits>.+?)</b>', url)
# if hits['hits'] != None:
#     hits['hits'] = hits['hits'].group('hits')
#     hits['hits'] = hits['hits'].replace(',', '')
#     hits['hits'] = int(hits['hits'])
# else:
#     hits['hits'] = 0
#
# print hits['hits']


import urllib2

from bs4 import BeautifulSoup


def get_alexa_linksin(domain):
    page = 0
    linksin = []

    while True:
        url = 'http://www.alexa.com/site/linksin;' + str(page) + '/' + domain
        req = urllib2.Request(url)
        HTML = urllib2.urlopen(req).read()
        soup = BeautifulSoup(HTML)

        next = soup.find(id='linksin').find('a', attrs={'class': 'next'})

        linksin += [(link['href'], link.string) for link in soup.find(id='linksin').findAll('a')]

        if next:
            page = page + 1
        else:
            break

    return linksin


if __name__ == '__main__':
    linksin = get_alexa_linksin('halotis.com')
    print linksin