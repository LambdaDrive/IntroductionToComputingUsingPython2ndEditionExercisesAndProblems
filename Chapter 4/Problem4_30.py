def distribution(filename):
    file = open(filename)
    content = file.read()
    file.close()
    numa = content.count('A ')
    numamin = content.count('A-')
    numbplus = content.count('B+')
    numb = content.count('B ')
    numbmin = content.count('B-')
    numc = content.count('C ')
    numcminus = content.count('C-')
    numf = content.count('F')
    print('{} students got A\n{} student got A-\n{} students got B+\n{} students got B\n{} students got B-\n{} students got C\n{} students got C-\n{} students got F'.format(numa, numamin,numbplus,numb,numbmin,numc,numcminus,numf))
    
                                                                                                                                                                             
