from urllib.request import urlopen
def getSource(url):
    'returns the content of resource specified by url as a string'
    response = urlopen(url)
    html = response.read()
    return html.decode()



from html.parser import HTMLParser
class LinkParser(HTMLParser):
    '''HTML doc parser that prints values of
       href attributes in anchor start tags'''

    def handle_starttag(self, tag, attrs):
        'print value of href attribute if any'
        
        if tag == 'a':                      # if anchor tag

            # search for href attribute and print its value
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])



from urllib.parse import urljoin
from html.parser import HTMLParser
class Collector(HTMLParser):
    'collects hyperlink URLs into a list'

    def __init__(self, url):
        'initializes parser, the url, and a list'
        HTMLParser.__init__(self)
        self.url = url
        self.links = []

        # Solution to Practice Problem 11.3        
        self.text = ''
        
    def handle_starttag(self, tag, attrs):
        'collects hyperlink URLs in their absolute format'
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    # construct absolute URL
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http': # collect HTTP URLs
                        self.links.append(absolute)
                        
    # Solution to Practice Problem 11.3        
    def handle_data(self, data):
        'collects and concatenates text data'
        self.text += data

    def getLinks(self):
        'returns hyperlinks URLs in their absolute format'
        return self.links

    # Solution to Practice Problem 11.3
    def getData(self):
        'returns the concatenation of all text data'
        return self.text



##################################
# Solutions to Practice Problems #
##################################


# Practice Problem 11.1
from urllib.request import urlopen
def news(url, topics):
    '''counts in resource with URL url the frequency
       of each topic in list topics'''
    # download and decode resource to obtain all lowercase content
    response = urlopen(url)
    html = response.read()
    content = html.decode().lower()

    for topic in topics: # find frequency of topic in content
        n = content.count(topic)
        print('{} appears {} times.'.format(topic, n))


# Practice Problem 11.2
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    'HTML doc parser that prints tags indented by depth'
    
    def __init__(self):
        'initializes the parser and the initial indentation'
        HTMLParser.__init__(self)
        self.indent = 0            # initial indentation value

    def handle_starttag(self, tag, attrs):
        '''prints start tag with an indentation proportional
           to the depth of the tag's element in the document'''
        if tag not in {'br', 'p'}:
            print('{}{} start'.format(self.indent*' ', tag))
            self.indent += 4

    def handle_endtag(self, tag):
        '''prints end tag with an indentation proportional
           to the depth of the tag's element in the document'''
        if tag not in {'br','p'}:
            self.indent -= 4
            print('{}{} end'.format(self.indent*' ', tag))


# Practice Problem 11.6
from re import findall
def frequency(content):
    '''returns dictionary containing frequencies
       of words in string content'''
    pattern = '[a-zA-Z]+'
    words = findall(pattern, content)
    dictionary = {}
    for w in words:
        if w in dictionary:
            dictionary[w] +=1
        else:
            dictionary[w] = 1
    return dictionary

