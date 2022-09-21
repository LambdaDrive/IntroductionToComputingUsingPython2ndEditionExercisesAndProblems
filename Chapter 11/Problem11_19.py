from re import findall

def emails(string):

    pattern = '\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'
    emaillist = findall(pattern, string)

    return emaillist

