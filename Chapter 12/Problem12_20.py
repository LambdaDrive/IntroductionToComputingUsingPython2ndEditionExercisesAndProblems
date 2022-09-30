import re
from multiprocessing import Process

def grep(textfile, regex):

    arquivo = open(textfile)
    content = arquivo.read()
    arquivo.close()

    content = content.split('\n')

    prog = re.compile(regex)

    listresult = []

    for line in content:
        if prog.search(line) != None:
            listresult.append(line)
    
    return listresult

def paralel(arquivo, regex):

    p = Process(target=grep, args=(arquivo, regex))
    p.start()
    p.join()
