def case(string):
    if string[0].isupper():
        return 'capitalized'
    elif string[0] in '0123456789':
        return 'unknown'
    else:
        return 'not captalized'
