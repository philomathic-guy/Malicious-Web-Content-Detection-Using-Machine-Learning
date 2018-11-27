# 1 stands for legitimate
# 0 stands for suspicious
# -1 stands for phishing

from bs4 import BeautifulSoup
import urllib, bs4, re
import socket

from google import google
import whois
from datetime import datetime
import time


def having_ip_address(url):
    match = re.search(
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)  # Ipv6
    if match:
        # print match.group()
        return -1
    else:
        # print 'No matching pattern found'
        return 1


def url_length(url):
    if len(url) < 54:
        return 1
    elif len(url) >= 54 | len(url) <= 75:
        return 0
    else:
        return -1


def shortening_service(url):
    match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                      'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                      'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                      'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                      'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                      'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                      'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                      'tr\.im|link\.zip\.net',
                      url)
    if match:
        return -1
    else:
        return 1


def having_at_symbol(url):
    match = re.search('@', url)
    if match:
        return -1
    else:
        return 1


def double_slash_redirecting(url):
    # since the position starts from, we have given 6 and not 7 which is according to the document
    list = [x.start(0) for x in re.finditer('//', url)]
    if list[len(list) - 1] > 6:
        return -1
    else:
        return 1


def prefix_suffix(domain):
    match = re.search('-', domain)
    if match:
        return -1
    else:
        return 1


def having_sub_domain(url):
    # Here, instead of greater than 1 we will take greater than 3 since the greater than 1 conition is when www and
    # country domain dots are skipped
    # Accordingly other dots will increase by 1
    if having_ip_address(url) == -1:
        match = re.search(
            '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
            '([01]?\\d\\d?|2[0-4]\\d|25[0-5]))|(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}',
            url)
        pos = match.end(0)
        url = url[pos:]
    list = [x.start(0) for x in re.finditer('\.', url)]
    if len(list) <= 3:
        return 1
    elif len(list) == 4:
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


def favicon(wiki, soup, domain):
    for head in soup.find_all('head'):
        for head.link in soup.find_all('link', href=True):
            dots = [x.start(0) for x in re.finditer('\.', head.link['href'])]
            if wiki in head.link['href'] or len(dots) == 1 or domain in head.link['href']:
                return 1
            else:
                return -1
    return 1


def https_token(url):
    match = re.search('https://|http://', url)
    if match.start(0) == 0:
        url = url[match.end(0):]
    match = re.search('http|https', url)
    if match:
        return -1
    else:
        return 1


def request_url(wiki, soup, domain):
    i = 0
    success = 0
    for img in soup.find_all('img', src=True):
        dots = [x.start(0) for x in re.finditer('\.', img['src'])]
        if wiki in img['src'] or domain in img['src'] or len(dots) == 1:
            success = success + 1
        i = i + 1

    for audio in soup.find_all('audio', src=True):
        dots = [x.start(0) for x in re.finditer('\.', audio['src'])]
        if wiki in audio['src'] or domain in audio['src'] or len(dots) == 1:
            success = success + 1
        i = i + 1

    for embed in soup.find_all('embed', src=True):
        dots = [x.start(0) for x in re.finditer('\.', embed['src'])]
        if wiki in embed['src'] or domain in embed['src'] or len(dots) == 1:
            success = success + 1
        i = i + 1

    for i_frame in soup.find_all('i_frame', src=True):
        dots = [x.start(0) for x in re.finditer('\.', i_frame['src'])]
        if wiki in i_frame['src'] or domain in i_frame['src'] or len(dots) == 1:
            success = success + 1
        i = i + 1

    try:
        percentage = success / float(i) * 100
    except:
        return 1

    if percentage < 22.0:
        return 1
    elif 22.0 <= percentage < 61.0:
        return 0
    else:
        return -1


def url_of_anchor(wiki, soup, domain):
    i = 0
    unsafe = 0
    for a in soup.find_all('a', href=True):
        # 2nd condition was 'JavaScript ::void(0)' but we put JavaScript because the space between javascript and ::
        # might not be
        # there in the actual a['href']
        if "#" in a['href'] or "javascript" in a['href'].lower() or "mailto" in a['href'].lower() or not (
                wiki in a['href'] or domain in a['href']):
            unsafe = unsafe + 1
        i = i + 1
        # print a['href']
    try:
        percentage = unsafe / float(i) * 100
    except:
        return 1
    if percentage < 31.0:
        return 1
        # return percentage
    elif 31.0 <= percentage < 67.0:
        return 0
    else:
        return -1


# Links in <Script> and <Link> tags
def links_in_tags(wiki, soup, domain):
    i = 0
    success = 0
    for link in soup.find_all('link', href=True):
        dots = [x.start(0) for x in re.finditer('\.', link['href'])]
        if wiki in link['href'] or domain in link['href'] or len(dots) == 1:
            success = success + 1
        i = i + 1

    for script in soup.find_all('script', src=True):
        dots = [x.start(0) for x in re.finditer('\.', script['src'])]
        if wiki in script['src'] or domain in script['src'] or len(dots) == 1:
            success = success + 1
        i = i + 1
    try:
        percentage = success / float(i) * 100
    except:
        return 1

    if percentage < 17.0:
        return 1
    elif 17.0 <= percentage < 81.0:
        return 0
    else:
        return -1


# Server Form Handler (SFH)
# Have written conditions directly from word file..as there are no sites to test ######
def sfh(wiki, soup, domain):
    for form in soup.find_all('form', action=True):
        if form['action'] == "" or form['action'] == "about:blank":
            return -1
        elif wiki not in form['action'] and domain not in form['action']:
            return 0
        else:
            return 1
    return 1


# Mail Function
# PHP mail() function is difficult to retrieve, hence the following function is based on mailto ######
def submitting_to_email(soup):
    for form in soup.find_all('form', action=True):
        if "mailto:" in form['action']:
            return -1
        else:
            return 1
    return 1


def abnormal_url(domain, url):
    hostname = domain.name
    match = re.search(hostname, url)
    if match:
        return 1
    else:
        return -1

# IFrame Redirection
def i_frame(soup):
    for i_frame in soup.find_all('i_frame', width=True, height=True, frameBorder=True):
        if i_frame['width'] == "0" and i_frame['height'] == "0" and i_frame['frameBorder'] == "0":
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
        rank = \
        bs4.BeautifulSoup(urllib.urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml").find(
            "REACH")['RANK']
    except TypeError:
        return -1
    rank = int(rank)
    if rank < 100000:
        return 1
    else:
        return 0


def google_index(url):
    site = google.search(url, 5)
    if site:
        return 1
    else:
        return -1


def statistical_report(url, hostname):
    url_match = re.search(
        'at\.ua|usa\.cc|baltazarpresentes\.com\.br|pe\.hu|esy\.es|hol\.es|sweddy\.com|myjino\.ru|96\.lt|ow\.ly', url)
    try:
        ip_address = socket.gethostbyname(hostname)
    except:
        print('Connection problem. Please check your internet connection!')
    ip_match = re.search(
        '146\.112\.61\.108|213\.174\.157\.151|121\.50\.168\.88|192\.185\.217\.116|78\.46\.211\.158|181\.174\.165\.13|46\.242\.145\.103|121\.50\.168\.40|83\.125\.22\.219|46\.242\.145\.98|'
        '107\.151\.148\.44|107\.151\.148\.107|64\.70\.19\.203|199\.184\.144\.27|107\.151\.148\.108|107\.151\.148\.109|119\.28\.52\.61|54\.83\.43\.69|52\.69\.166\.231|216\.58\.192\.225|'
        '118\.184\.25\.86|67\.208\.74\.71|23\.253\.126\.58|104\.239\.157\.210|175\.126\.123\.219|141\.8\.224\.221|10\.10\.10\.10|43\.229\.108\.32|103\.232\.215\.140|69\.172\.201\.153|'
        '216\.218\.185\.162|54\.225\.104\.146|103\.243\.24\.98|199\.59\.243\.120|31\.170\.160\.61|213\.19\.128\.77|62\.113\.226\.131|208\.100\.26\.234|195\.16\.127\.102|195\.16\.127\.157|'
        '34\.196\.13\.28|103\.224\.212\.222|172\.217\.4\.225|54\.72\.9\.51|192\.64\.147\.141|198\.200\.56\.183|23\.253\.164\.103|52\.48\.191\.26|52\.214\.197\.72|87\.98\.255\.18|209\.99\.17\.27|'
        '216\.38\.62\.18|104\.130\.124\.96|47\.89\.58\.141|78\.46\.211\.158|54\.86\.225\.156|54\.82\.156\.19|37\.157\.192\.102|204\.11\.56\.48|110\.34\.231\.42',
        ip_address)
    if url_match:
        return -1
    elif ip_match:
        return -1
    else:
        return 1


def main(url):
    # url = sys.argv[1]
    with open('/opt/lampp/htdocs/BE/markup.txt', 'r') as file:
        soup_string = file.read()

    soup = BeautifulSoup(soup_string, 'html.parser')

    status = []

    hostname = url
    h = [(x.start(0), x.end(0)) for x in re.finditer('https://|http://|www.|https://www.|http://www.', hostname)]
    z = int(len(h))
    if z != 0:
        y = h[0][1]
        hostname = hostname[y:]
        h = [(x.start(0), x.end(0)) for x in re.finditer('/', hostname)]
        z = int(len(h))
        if z != 0:
            hostname = hostname[:h[0][0]]

    status.append(having_ip_address(url))
    status.append(url_length(url))
    status.append(shortening_service(url))
    status.append(having_at_symbol(url))
    status.append(double_slash_redirecting(url))
    status.append(prefix_suffix(hostname))
    status.append(having_sub_domain(url))

    dns = 1
    try:
        domain = whois.query(hostname)
    except:
        dns = -1

    if dns == -1:
        status.append(-1)
    else:
        status.append(domain_registration_length(domain))

    status.append(favicon(url, soup, hostname))
    status.append(https_token(url))
    status.append(request_url(url, soup, hostname))
    status.append(url_of_anchor(url, soup, hostname))
    status.append(links_in_tags(url, soup, hostname))
    status.append(sfh(url, soup, hostname))
    status.append(submitting_to_email(soup))

    if dns == -1:
        status.append(-1)
    else:
        status.append(abnormal_url(domain, url))

    status.append(i_frame(soup))

    if dns == -1:
        status.append(-1)
    else:
        status.append(age_of_domain(domain))

    status.append(dns)

    status.append(web_traffic(soup))
    status.append(google_index(url))
    status.append(statistical_report(url, hostname))

    print('\n1. Having IP address\n2. URL Length\n3. URL Shortening service\n4. Having @ symbol\n'
          '5. Having double slash\n6. Having dash symbol(Prefix Suffix)\n7. Having multiple subdomains\n'
          '8. SSL Final State\n8. Domain Registration Length\n9. Favicon\n10. HTTP or HTTPS token in domain name\n'
          '11. Request URL\n12. URL of Anchor\n13. Links in tags\n14. SFH\n15. Submitting to email\n16. Abnormal URL\n'
          '17. IFrame\n18. Age of Domain\n19. DNS Record\n20. Web Traffic\n21. Google Index\n22. Statistical Reports\n')
    print(status)
    return status


if __name__ == "__main__":
    main()
