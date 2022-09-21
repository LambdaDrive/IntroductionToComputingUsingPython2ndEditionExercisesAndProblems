from urllib.request import urlopen
from re import findall
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def handle_data(self, data):
        print(data)

def getContent(URL):
    response = urlopen(URL)
    html = response.read()
    content = html.decode()
    parser = MyHTMLParser()
    parser.feed(content)
    
