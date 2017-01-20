import urllib, sys, bs4

rank= bs4.BeautifulSoup(urllib.urlopen("http://data.alexa.com/data?cli=10&dat=s&url="+ sys.argv[1]).read(), "xml").find("REACH")['RANK']
print rank


