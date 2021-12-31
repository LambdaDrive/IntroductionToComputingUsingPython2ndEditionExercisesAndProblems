def reverse(phonebook):
    keys = phonebook.keys()
    newdic = {}
    for key in keys:
        newdic[phonebook[key]] = key
    return newdic
