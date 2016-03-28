#just a note file about beautifulsoup

from bs4 import BeautifulSoup
import urllib2

url = "http://www.circusautomatic.com/research.php"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

print soup.prettify()

for link in soup.find_all('a'):
    print(link.get('href'))
