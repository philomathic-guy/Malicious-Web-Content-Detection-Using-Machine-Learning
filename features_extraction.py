#1 stands for legitimate
#0 stands for suspicious
#-1 stands for phishing

import re
import urllib2
import re
from bs4 import BeautifulSoup

def having_ip_address(url):
    match=re.search('(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5]))|(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}',url)
    #IP address outside the permissible range condition not added yet. Eg. 999.400.500.260 will also be an IP address
    #If more than 3 digits in IP address, then it takes only 3 digits and proceeds. BUT IT SHOULD SHOW NOT A MATCH. CHECK!
    if match:
        #print match.group()
        return -1
    else:
        #print 'No matching pattern found'
        return 1

def url_length(url):
    if len(url)<54:
        return 1
    elif len(url)>=54|len(url)<=75:
        return 0
    else:
        return -1


def shortening_service(url):
#These form the maximum used URL shortening serivices. If possible, find more
    match=re.search('bit\.ly|goo\.gl|ow\.ly|t\.co|tinyurl|tr\.im',url)
    if match:
        return -1
    else:
        return 1

def having_at_symbol(url):
    match=re.search('@',url)
    if match:
        return -1
    else:
        return 1

def double_slash_redirecting(url):
#since the position starts from, we have given 6 and not 7 which is according to the document
    list=[x.start(0) for x in re.finditer('//', url)]
    if list[len(list)-1]>6:
        return -1
    else:
        return 1

def prefix_suffix(url):
    match=re.search('-',url)
    if match:
        return -1
    else:
        return 1

def having_sub_domain(url):
#Here, instead of greater than 1 we will take greater than 3 since the greater than 1 conition is when www and country domain dots are skipped
#Accordingly other dots will increase by 1
    if having_ip_address(url)==-1:
        match=re.search('(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5]))|(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}',url)
        pos=match.end(0)
        url=url[pos:]
    list=[x.start(0) for x in re.finditer('\.',url)]
    if len(list)<=3:
        return 1
    elif len(list)==4:
        return 0
    else:
        return -1

#SSL FINAL STATE

#DOMAIN REGISTRATION LENGTH

def favicon(wiki, soup):
   for head in soup.find_all('head'):
      for head.link in soup.find_all('link', href=True):
         dots = [x.start(0) for x in re.finditer('\.', head.link['href'])]
         if wiki in head.link['href'] or len(dots) == 1:
            return 1
         else:
            return -1

#PORT

def https_token(url):
    match=re.search('https://|http://',url)
    if match.start(0)==0:
        url=url[match.end(0):]
    match=re.search('http|https',url)
    if match:
        return -1
    else:
        return 1

##################
def request_url(wiki, soup):
   i = 0
   success = 0
   for img in soup.find_all('img', src= True):
      if wiki in img['src']:
         success = success + 1
      i=i+1
##################

def main():
    status=[]
    url="https://www.http-spit.ac.in"
    status.append(having_ip_address(url))
    status.append(url_length(url))
    status.append(shortening_service(url))
    status.append(having_at_symbol(url))
    status.append(double_slash_redirecting(url))
    status.append(prefix_suffix(url))
    status.append(having_sub_domain(url))

    #wiki = "http://www.scluster.com/"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    status.append(favicon(url,soup))

    status.append(https_token(url))
################
    status.append(request_url(url, soup))
################
    print '\n1. Having IP address\n2. URL Length\n3. URL Shortening service\n4. Having @ symbol\n5. Having double slash\n6. Having dash symbol(Prefix Suffix)\n7. Having multiple subdomains'
    print '\n8. HTTP or HTTPS token in domain name\n'
    print status

if __name__ == "__main__":
    main()