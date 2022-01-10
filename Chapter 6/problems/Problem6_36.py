def caesar(n, textfile):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    alphabetreal = 'abcdefghijklmnopqrstuvwxyz'
    translationtable = ''
    for i in range(int(len(alphabet)/2)):
        translationtable += alphabet[i+n]
    alphabetreal += alphabetreal.upper()
    translationtable += translationtable.upper()
    table = str.maketrans(alphabetreal, translationtable)
    file = open(textfile)
    content = file.read()
    file.close()
    content = content.translate(table)
    print(content)
    file = open('cipher.txt', 'w')
    file.write(content)
    file.close()
