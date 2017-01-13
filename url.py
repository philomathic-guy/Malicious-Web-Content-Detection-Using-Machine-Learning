#1 stands for legitimate
#0 stands for suspicious
#-1 stands for phishing

import re

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

def shortened_url(url):
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

def having_doubleslash(url):
#since the position starts from, we have given 6 and not 7 which is according to the document
    list=[x.start(0) for x in re.finditer('//', url)]
    if list[len(list)-1]>6:
        return -1
    else:
        return 1

def having_dash_symbol(url):
    match=re.search('-',url)
    if match:
        return -1
    else:
        return 1

def subdomains(url):
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

def main():
    status=[]
    url=raw_input("Enter the url :")
    status.append(having_ip_address(url))
    status.append(url_length(url))
    status.append(having_at_symbol(url))
    status.append(having_doubleslash(url))
    status.append(having_dash_symbol(url))
    status.append(subdomains(url))
    status.append(shortened_url(url))
    print '\n1. Having IP address\n2. URL Length\n3. Having @ symbol\n4. Having double slash\n5. Having dash symbol\n6. Having multiple subdomains\n7. URL Shortened\n'
    print status

if __name__ == "__main__":
    main()