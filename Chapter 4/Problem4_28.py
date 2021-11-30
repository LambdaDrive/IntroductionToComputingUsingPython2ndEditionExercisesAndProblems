def links(htmlfile):
    file = open(htmlfile)
    content = file.read()
    file.close()
    return content.count('</a>')
