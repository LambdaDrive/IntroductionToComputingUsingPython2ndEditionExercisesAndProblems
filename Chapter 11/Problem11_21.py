from urllib.parse import urljoin
from theml.parser import HTMLParser
from urllib.request import urlretrieve

class Collector(HTMLParser):
    
    def __init__(self, url):
        HTMLParser.__init__(self)
        self.url = url
        self.links = []

    def handle_starttag(self, tag, attrs):

        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http':
                        self.links.append(absolute)

    def getLinks(self):
        return self.links

def download(url):
    
    links = []
    morelinks = []
    coletor = Collector(url)
    links.append(coletor.getLinks())
    for link in links:
        coletor = Collector(url)
        morelinks.append(coletor.getLinks())
    links.append(morelinks)
    for link in links:
        urlretrieve(link)

