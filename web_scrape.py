# -1 => Phishing
#  0 => Suspicious
# +1 => Legitimate

import urllib2
import re
from bs4 import BeautifulSoup

# Request URL
# Following is for images
# For Videos : embed, a, iframes, video... these tags can be used
# What to do??
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
   percentage = success/float(i) * 100

   if percentage < 22.0 :
      return -1
   elif((percentage >= 22.0) and (percentage < 61.0)) :
      return 0
   else :
      return 1

# URL of Anchor
def url_anchor(wiki, soup):
   i = 0
   success = 0
   for a in soup.find_all('a', href= True):
      if wiki in a['href']:
         success = success + 1
      i=i+1
      #print a['href']
   percentage = success/float(i) * 100
   if percentage < 31.0 :

      return -1
   elif((percentage >= 31.0) and (percentage < 67.0)) :
      return 0
   else :
      return 1

# Links in <Script> and <Link> tags
# <Meta> has no links in most of the websites..so can't compare with domain names
def script_link_links(wiki, soup):
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
   percentage = success/float(i) * 100

   if percentage < 17.0 :
      return -1
   elif((percentage >= 17.0) and (percentage < 81.0)) :
      return 0
   else :
      return 1

# Server Form Handler (SFH)
# Have written consitions directly from word file..as there are no sites to test
def sfh(wiki, soup):
   for form in soup.find_all('form', action= True):
      if form['action'] =="" or form['action'] == "about:blank" :
         return -1
      elif wiki not in form['action']:
          return 0
      else:
            return 1
   return 1

#Favicon
#This function clashes with the Link Tag feature..What to do?
def favicon(wiki, soup):
   for head in soup.find_all('head'):
      for head.link in soup.find_all('link', href=True):
         dots = [x.start(0) for x in re.finditer('\.', head.link['href'])]
         if wiki in head.link['href'] or len(dots) == 1:
            return 1
         else:
            return -1


#Mail Function
#PHP mail() function is difficult to retreive, hence the following function is based on mailto
def mail(wiki, soup):
   for form in soup.find_all('form', action= True):
      if "mailto:" in form['action'] :
         return -1
      else:
          return 1
   return 1

#IFrame Redirection
 #Checking remaining
def iframe_redirection(wiki, soup):
    for iframe in soup.find_all('iframe', width=True, height=True, frameBorder=True):
        if iframe['width']=="0" and iframe['height']=="0" and iframe['frameBorder']=="0":
            return -1
        else:
            return 0
    return 0


def main():
   status=[]
   wiki = "http://www.scluster.com/"
   page = urllib2.urlopen(wiki)
   soup = BeautifulSoup(page)
   print "1. Request Url\n2. Anchor tag Url\n3. Script and link tag links\n4. Server form handler\n5. Favicon\n6. Mail\n7.iFrame Redirection "
   status.append(request_url(wiki, soup))
   status.append(url_anchor(wiki, soup))
   status.append(script_link_links(wiki, soup))
   status.append(sfh(wiki, soup))
   status.append(favicon(wiki, soup))
   status.append(mail(wiki,soup))
   status.append(iframe_redirection(wiki, soup))
   print status

if __name__ == "__main__":
    main()