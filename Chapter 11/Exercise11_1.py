from urllib.request import urlopen
def news(url, words):
    response = urlopen(url)
    html = response.read()
    html = html.decode()
    word = []
    for wor in words:
        word.append([wor, html.count(wor)])
    for couple in word:
        print ('{} appears {} times.'.format(couple[0], couple[1]))
    
