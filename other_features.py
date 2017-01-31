import OpenSSL, ssl, sys
import re
import urllib, sys, bs4
from google import search

def ssl_feature(url):

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

def webtraffic_feature(url):
    try:
        rank = bs4.BeautifulSoup(urllib.urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml").find("REACH")['RANK']
    except TypeError:
        return -1
    rank= int(rank)
    if (rank<100000):
        return 1
    else:
        return 0

def googleindex_feature(url):
    site= search(url, stop=5)
    if site:
        return 1
    else:
        return -1


def main():
    status=[]
    url="https://www.google.com"
    status.append(ssl_feature(url))
    status.append(webtraffic_feature(url))
    status.append(googleindex_feature(url))
    print '\n1. HTTPS (Hyper Text Transfer Protocol with Secure Sockets Layer)  \n2. WebTraffic\n3. Google Index'
    print status

if __name__ == "__main__":
    main()