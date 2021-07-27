def reverse_string(string):
    s = [3]    
    for letter in range(1, 3):
        s[(letter)-1]=string[-(letter)]
    
    return s
