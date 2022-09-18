import time
import re

def timing(func, n):
    'runs func on input returned by buildInput'
    funcInput = n  # obtain input for func 

    start = time.time()        # take start time
    func(funcInput)            # run func on funcInput
    end = time.time()          # take end time
    timefinal = float(end) - float(start)
    return timefinal         # return execution time

def maketransreplace(string):
    
    table = str.maketrans('!,.:;?', 6*' ')
    stringue = string.translate(table)

def replacereplace(string):

    string = string.replace('!,.:;?', 6*' ')

def regex(string):
    
    prog = re.compile('[a-zA-Z]*')
    result = prog.match(string)

print(timing(maketransreplace, 'texto com pontuacao! \n mais pontuacao? \n talvez, mais, pontuacao?'))
print(timing(replacereplace, 'texto com pontuacao! \n mais pontuacao? \n talvez, mais, pontuacao?'))
print(timing(regex, 'texto com pontuacao! \n mais pontuacao? \n talvez, mais, pontuacao?'))
