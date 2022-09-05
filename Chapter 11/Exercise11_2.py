from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.space = 0
    
    def handle_starttag(self, tag, attrs):

        if tag not in {'br', 'p'}:
            print('{} {} start'.format(' ' *self.space, tag))
            self.space += 4
        
    def handle_endtag(self, tag):

        if tag not in {'br', 'p'}:
            self.space -= 4
            print('{} {} end'.format(' ' *self.space, tag))
            
