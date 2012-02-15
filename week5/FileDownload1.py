import urllib2
from BeautifulSoup import BeautifulSoup

from urlparse import *

from urllib import urlretrieve
import os
import sys


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
        myUrl = myUrl[:0] + myUrl[:myUrl.find(">")-1] 
        myUrl = urljoin(site, myUrl)
        fileName = myUrl.split("/")
        fileName = fileName[-1]
        print fileName
        folder = 'C:/Temp/'
        folder = folder + "/" +  fileName
        
        urlretrieve(myUrl, folder)
 
#print soup.prettify()
