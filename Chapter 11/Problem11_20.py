from re import search
from urllib.request import urlopen

def bestprice(listaddress, listprices):
            
    for i in range(len(listaddress)):
        
        response = urlopen(listaddress[i])
        html = response.read()
        html = html.decode()
        match = search('[0-9]?,?[0-9]*.[0-9][0-9]', html)
        currentprice = match.string[match.start():match.end()]
        if currentprice < listprices[i]:
            print(listaddress[i])
