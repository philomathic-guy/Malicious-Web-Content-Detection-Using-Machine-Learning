from selenium import webdriver
import urllib2, httplib

#condition for more than 1 redirect is left. Looking for a url which redirects more than once.
def redirect(url):
    httplib.HTTPConnection.debuglevel = 1
    request = urllib2.Request(url)
    opener = urllib2.build_opener()
    f=opener.open(request)
    print f.url
    return 1

def on_mouseover(page_source_with_js):
    print 'HI'

def main():
    status = []
    url = 'http://ow.ly/gxoS308a1EM'

    driver = webdriver.PhantomJS()
    driver.get(url)
    page_source_with_js=driver.page_source

    status.append(on_mouseover(page_source_with_js))
    status.append(redirect(url))

if __name__ == "__main__":
    main()