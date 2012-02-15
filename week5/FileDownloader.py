import urllib2
from BeautifulSoup import BeautifulSoup

from urlparse import *

from urllib import urlretrieve
import os
import sys

folder = 'C://Documents and Settings//PSRCuser.PSRC3652//uw_python//Download'
site = 'http://jon-jacky.github.com/uw_python/winter_2012/index.html'
page = urllib2.urlopen(site).read()
soup = BeautifulSoup(page)
anchors = soup.findAll('a')
o = urlparse(site)
print type (anchors)
for item in anchors:
    myUrl = str(item)
    if myUrl.rfind('.py<') != -1:
        myUrl = myUrl[myUrl.find("=")+2:]
        myUrl = myUrl[:0] + myUrl[:myUrl.find(">")]
        myUrl = urljoin(site, myUrl)
        print myUrl
        urlretrieve(myUrl, folder)
o = urlparse(site)
myUrl = o.scheme 
#print soup.prettify()
