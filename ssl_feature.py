import OpenSSL, ssl, sys
import re

hostname=sys.argv[1]
h=[(x.start(0),x.end(0)) for x in re.finditer('https://|http://',hostname)]
z=int(len(h))
print z
if z!=0:
	y=h[0][1]
	host= "www."
	hostname=hostname[y:]
	hostname=host+hostname
	print hostname
	h=[(x.start(0),x.end(0)) for x in re.finditer('/',hostname)]
	y=h[0][0]
	hostname=hostname[:y]

cert = ssl.get_server_certificate((hostname, 443))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
i=x509.get_issuer()
before=x509.get_notBefore()
after=x509.get_notAfter()

issuer=str(i)
notBefore=str(before)
notAfter=str(after)

r=issuer.split("'")
r=r[1]
ca=r.split("CN=")
certificate_authority=ca[1]
print certificate_authority

notBefore=notBefore[:4]
notAfter=notAfter[:4]
if (int(notAfter)-int(notBefore)>=2):
	print "safe"
else:
	print "phishing"
print issuer
print notBefore
print notAfter
