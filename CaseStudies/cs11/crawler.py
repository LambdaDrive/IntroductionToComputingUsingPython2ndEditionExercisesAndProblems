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

from urllib.parse import urljoin
from html.parser import HTMLParser
class Collector(HTMLParser):
    'collects hyperlink URLs into a list'

    def __init__(self, url):
        'initializes parser, the url, and a list'
        HTMLParser.__init__(self)
        self.url = url
        self.links = []

        # Solution to practice problem 11.3        
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
                        
    # Solution to practice problem 11.3        
    def handle_data(self, data):
        'collects and concatenates text data'
        self.text += data

    def getLinks(self):
        'returns hyperlinks URLs in their absolute format'
        return self.links

    # Solution to practice problem 11.3
    def getData(self):
        'returns the concatenation of all text data'
        return self.text



from urllib.request import urlopen
def analyze(url):
    '''prints the frequency of every word in web page url and
       prints and returns the list of http links, in absolute
       format, in it'''
    
    print('\n\nVisiting', url)      # for testing

    # obtain links in the web page
    content = urlopen(url).read().decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.getLinks()     # get list of links

    # compute word frequencies
    content = collector.getData()   # get text data as a string
    freq = frequency(content)

    # print the frequency of every text data word in web page
    print('\n{:45} {:10} {:5}'.format('URL', 'word', 'count'))
    for word in freq:
        print('{:45} {:10} {:5}'.format(url, word, freq[word]))

    # print the http links found in web page
    print('\n{:45} {:10}'.format('URL', 'link'))
    for link in urls:
        print('{:45} {:10}'.format(url, link))

    return urls



def crawl1(url):
    'recursive web crawler that calls analyze() on every web page'

    # analyze() returns a list of hyperlink URLs in web page url 
    links = analyze(url)

    # recursively continue crawl from every link in links
    for link in links:
        try:  # try block because link may not be valid HTML file
            crawl1(link)   
        except:           # if an exception is thrown,
            pass          # ignore and move on.



visited = set()              # initialize visited to an empty set

def crawl2(url):
    '''a recursive web crawler that calls analyze()
       on every visited web page'''

    # add url to set of visited pages
    global visited     # while not necessary, warns the programmer 
    visited.add(url)

    # analyze() returns a list of hyperlink URLs in web page url 
    links = analyze(url)

    # recursively continue crawl from every link in links
    for link in links:
        # follow link only if not visited
        if link not in visited:
            try:
                crawl2(link)
            except:
                pass



##################################
# Solutions to Practice Problems #
##################################


# Practice Problem CS.58
class Crawler2:
    'a web crawler'
    
    def __init__(self):
        'initializes set visited to an empty set'
        self.visited = set()
        
    def crawl(self, url):
        '''calls analyze() on web page url and calls itself
           on every link to an unvisited web page'''
        links = analyze(url)
        self.visited.add(url)
        for link in links:
            if link not in self.visited:
                try:
                    self.crawl(link)
                except:
                    pass
