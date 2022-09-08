from urllib.parse import urljoin
from html.parser import HTMLParser

class Collector(HTMLParser):

    def __init__(self, url):
        
        HTMLParser.__init__(self)
        self.url = url
        self.links = []
        self.text = ''

    def handle_starttag(self, tag, attrs):
        
        if tag == 'a':
            for attr in atrrs:
                if attr[0] == 'href':
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http':
                        self.links.append(absolute)
    def getLinks(self):
        
        return self.links

    def handle_data(self, data):

        self.text += data

    def getData(self):
        return self.text

