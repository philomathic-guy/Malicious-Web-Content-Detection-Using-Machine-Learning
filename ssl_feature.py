import OpenSSL, ssl, sys
import re

hostname=sys.argv[1]
h=[(x.start(0),x.end(0)) for x in re.finditer('https://|http://',hostname)]
z=int(len(h))
if z!=0:
    y=h[0][1]
    print y
    if y==7:
        https=0
    else:
        https=1
    host= "www."
    hostname=hostname[y:]
    hostname=host+hostname
    print hostname
    h = [(x.start(0), x.end(0)) for x in re.finditer('/', hostname)]
    z=int(len(h))
    if z!=0:
        hostname=hostname[:h[0][0]]
else:
    https=0


cert = ssl.get_server_certificate((hostname, 443))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
i=x509.get_issuer()
before=x509.get_notBefore()
after=x509.get_notAfter()

issuer=str(i)
notBefore=str(before)
notAfter=str(after)
print notBefore
print notAfter

r=issuer.split("'")
r=r[1]
ca=r.split("CN=")
certificate_authority=ca[1]
print certificate_authority

h=[x.start(0) for x in re.finditer('Comodo|Symantec|GoDaddy|GlobalSign|IdenTrust|DigiCert|StartCom|Entrust|Trustwave|Verizon|Secom|Unizeto|QuoVadis|Deutsche Telekom|Network Solutions|TWCA|VeriSign|GeoTrust|Thawte|Doster|Google',certificate_authority)]
z=int((len(h)))
if z!=0:
	check=1
else:
    check=0
notBefore=notBefore[:4]
notAfter=notAfter[:4]
if (int(notAfter)-int(notBefore)>=1 and check==1 and https==1):
	print 1
elif https==1 :
    print 0
else:
	print -1
