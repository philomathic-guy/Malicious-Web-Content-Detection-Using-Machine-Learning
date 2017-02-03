#1 stands for legitimate
#0 stands for suspicious
#-1 stands for phishing

from bs4 import BeautifulSoup
from selenium import webdriver
import re, urllib2, httplib
import OpenSSL, ssl
import urllib, sys, bs4

from google import google
import whois
from datetime import datetime
import time

def having_ip_address(url):
    match=re.search('(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  #IPv4
                    '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)'  #IPv4 in hexadecimal
                    '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}',url)     #Ipv6
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
    match=re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                    'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                    'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                    'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                    'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                    'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                    'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|tr\.im|link\.zip\.net',url)
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

def sslfinal_state(url):
    hostname = url
    h = [(x.start(0), x.end(0)) for x in re.finditer('https://|http://', hostname)]
    z = int(len(h))
    if z != 0:
        y = h[0][1]
        if y == 7:
            https = 0
        else:
            https = 1
        host = "www."
        hostname = hostname[y:]
        hostname = host + hostname
        #print hostname
        h = [(x.start(0), x.end(0)) for x in re.finditer('/', hostname)]
        z = int(len(h))
        if z != 0:
            hostname = hostname[:h[0][0]]
    else:
        https = 0
    try:
        cert = ssl.get_server_certificate((hostname, 443))
    except:
        return
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    i = x509.get_issuer()
    before = x509.get_notBefore()
    after = x509.get_notAfter()

    issuer = str(i)
    notBefore = str(before)
    notAfter = str(after)
    print notBefore
    print notAfter

    r = issuer.split("'")
    r = r[1]
    ca = r.split("CN=")
    certificate_authority = ca[1]
    print certificate_authority

    h = [x.start(0) for x in re.finditer(
        'Comodo|Symantec|GoDaddy|GlobalSign|IdenTrust|DigiCert|StartCom|Entrust|Trustwave|Verizon|Secom|Unizeto|QuoVadis|Deutsche Telekom|Network Solutions|TWCA|VeriSign|GeoTrust|Thawte|Doster|Google',
        certificate_authority)]
    z = int((len(h)))
    if z != 0:
        check = 1
    else:
        check = 0
    notBefore = notBefore[:4]
    notAfter = notAfter[:4]
    if (int(notAfter) - int(notBefore) >= 1 and check == 1 and https == 1):
        return 1
    elif https == 1:
        return 0
    else:
        return -1

def domain_registration_length(domain):
    expiration_date = domain.expiration_date
    today = time.strftime('%Y-%m-%d')
    today = datetime.strptime(today, '%Y-%m-%d')
    registration_length = abs((expiration_date - today).days)

    if registration_length / 365 <= 1:
        return -1
    else:
        return 1


def favicon(wiki, soup):
   for head in soup.find_all('head'):
      for head.link in soup.find_all('link', href=True):
         dots = [x.start(0) for x in re.finditer('\.', head.link['href'])]
         if wiki in head.link['href'] or len(dots) == 1:
            return 1
         else:
            return -1

def https_token(url):
    match=re.search('https://|http://',url)
    if match.start(0)==0:
        url=url[match.end(0):]
    match=re.search('http|https',url)
    if match:
        return -1
    else:
        return 1

def request_url(wiki, soup):
   i = 0
   success = 0
   for img in soup.find_all('img', src= True):
      if wiki in img['src']:
         success = success + 1
      i=i+1
      #print a['href']

   for audio in soup.find_all('audio', src= True):
      if wiki in audio['src']:
         success = success + 1
      i=i+1

   for embed in soup.find_all('embed', src= True):
      dots=[x.start(0) for x in re.finditer('\.',embed['src'])]
      if wiki in embed['src'] or len(dots)==1:
         success = success + 1
      i=i+1

   for iframe in soup.find_all('iframe', src= True):
      dots=[x.start(0) for x in re.finditer('\.',iframe['src'])]
      if wiki in iframe['src'] or len(dots)==1:
         success = success + 1
      i=i+1

   for video in soup.find_all('video', loop=True):
      percentage = percentage +1
      print percentage
   try:
      percentage = success/float(i) * 100
   except:
       return 1

   if percentage < 22.0 :
      return -1
   elif((percentage >= 22.0) and (percentage < 61.0)) :
      return 0
   else :
      return 1

def url_of_anchor(wiki, soup):
    i = 0
    success = 0
    for a in soup.find_all('a', href=True):
        if wiki in a['href']:
            success = success + 1
        i = i + 1
        # print a['href']
    try:
        percentage = success / float(i) * 100
    except:
        return 1
    if percentage < 31.0:

        return -1
    elif ((percentage >= 31.0) and (percentage < 67.0)):
        return 0
    else:
        return 1

# Links in <Script> and <Link> tags
###### <Meta> has no links in most of the websites..so can't compare with domain names ######
def links_in_tags(wiki, soup):
   i=0
   success =0
   for link in soup.find_all('link', href= True):
      if wiki in link['href']:
         success = success + 1
      i=i+1

   for script in soup.find_all('script', src= True):
      if wiki in script['src']:
         success = success + 1
      i=i+1
   try:
       percentage = success / float(i) * 100
   except:
       return 1

   if percentage < 17.0 :
      return -1
   elif((percentage >= 17.0) and (percentage < 81.0)) :
      return 0
   else :
      return 1

# Server Form Handler (SFH)
###### Have written consitions directly from word file..as there are no sites to test ######
def sfh(wiki, soup):
   for form in soup.find_all('form', action= True):
      if form['action'] =="" or form['action'] == "about:blank" :
         return -1
      elif wiki not in form['action']:
          return 0
      else:
            return 1
   return 1

#Mail Function
###### PHP mail() function is difficult to retreive, hence the following function is based on mailto ######
def submitting_to_email(soup):
   for form in soup.find_all('form', action= True):
      if "mailto:" in form['action'] :
         return -1
      else:
          return 1
   return 1

###### ABNORMAL URL ######

###### condition for more than 1 redirect is left. Looking for a url which redirects more than once ######
def redirect(url):
    httplib.HTTPConnection.debuglevel = 1
    request = urllib2.Request(url)
    opener = urllib2.build_opener()
    f=opener.open(request)
    print f.url
    return 1

#IFrame Redirection
###### Checking remaining on some site######
def iframe(soup):
    for iframe in soup.find_all('iframe', width=True, height=True, frameBorder=True):
        if iframe['width']=="0" and iframe['height']=="0" and iframe['frameBorder']=="0":
            return -1
        else:
            return 1
    return 1


def age_of_domain(domain):
    creation_date = domain.creation_date
    expiration_date = domain.expiration_date
    ageofdomain = abs((expiration_date - creation_date).days)
    if ageofdomain / 30 < 6:
        return -1
    else:
        return 1


def web_traffic(url):
    try:
        rank = bs4.BeautifulSoup(urllib.urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml").find("REACH")['RANK']
    except TypeError:
        return -1
    rank= int(rank)
    if (rank<100000):
        return 1
    else:
        return 0

def google_index(url):
    site=google.search(url, 5)
    if site:
        return 1
    else:
        return -1

##### LINKS PONITING TO PAGE #####

##### STATISTICAL REPORT ######

def main():
    status=[]
    url="http://www.spit.ac.in"
    status.append(having_ip_address(url))
    status.append(url_length(url))
    status.append(shortening_service(url))
    status.append(having_at_symbol(url))
    status.append(double_slash_redirecting(url))
    status.append(prefix_suffix(url))
    status.append(having_sub_domain(url))
    status.append(sslfinal_state(url))
    dns=1
    try:
        domain = whois.query("dbfjefklj.com")
    except:
        dns=-1

    if dns==-1:
        status.append(-1)
    else:
        status.append(domain_registration_length(domain))

    #wiki = "http://www.scluster.com/"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)

    status.append(favicon(url,soup))
    status.append(https_token(url))
    status.append(request_url(url, soup))
    status.append(url_of_anchor(url, soup))
    status.append(links_in_tags(url,soup))
    status.append(sfh(url,soup))
    status.append(submitting_to_email(soup))
    status.append(redirect(url))
    status.append(iframe(soup))

    if dns == -1:
        status.append(-1)
    else:
        status.append(age_of_domain(domain))

    status.append(dns)

    status.append(web_traffic(soup))
    status.append(google_index(url))


    print '\n1. Having IP address\n2. URL Length\n3. URL Shortening service\n4. Having @ symbol\n5. Having double slash\n' \
          '6. Having dash symbol(Prefix Suffix)\n7. Having multiple subdomains\n8. SSL Final State\n' \
          '9. Favicon\n10. HTTP or HTTPS token in domain name\n11. Request URL\n12. URL of Anchor\n13. Links in tags\n' \
          '14. SFH\n15. Submitting to email\n16. Redirect\n17. IFrame\n18. Web Traffic\n19. Google Index'
    print status

if __name__ == "__main__":
    main()