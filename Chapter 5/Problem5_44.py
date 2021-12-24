def cipher(cifra, cifrar):
    table = str.maketrans('0123456789', cifra)
    return cifrar.translate(table)
