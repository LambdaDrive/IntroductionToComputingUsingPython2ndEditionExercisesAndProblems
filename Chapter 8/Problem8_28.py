class Textfile:

    def __init__(self, filename):

        file = open(filename)
        content = file.read()
        file.close
        self.file = content

    def nchars(self):

        charnum = 0
        content = self.file
        charnum = len(content)
        return charnum

    def nwords(self):

        numwords = 0
        content= self.file
        content = content.split()
        numwords = len(content)
        return numwords

    def nlines(self):

        numlines = 0
        content = self.file
        content = content.split('\n')
        numlines = len(content)
        return numlines

    def read(self):

        return self.file

    def readlines(self, n):

        content = self.file
        content = content.split('\n')
        return content

    def grep(self, string):

        result = ''
        lines = []
        content = self.file
        content = content.split('\n')
        for i in range(len(content)):
            if string in content[i]:
                lines.append(i)
        for line in lines:
            result += '{}: '.format(line)
            result +='{} \n'.format(content[line])
        print(result)

    def words(self):

        content = self.file
        content = content.split()
        content = list(set(content))
        return content
    
    def occurrences(self):

        ocur = {}
        content = self.file
        content = content.split()
        content = set(content)
        for word in content:
            ocur[word] = 0
        content = self.file.split()
        for word in content:
            ocur[word] += 1
        return ocur

    def average(self):
        content = self.file
        for symbol in '.?!':
            content = content.replace(symbol, '%')
        content = content.replace('\n', '')
        content = content.split('%')
        avg = 0
        wordssentence = []
        morewords = 0
        fewerwords = 100
        for i in range(len(content)-1):
            wordssentence.append(content[i].split())
        for listwords in wordssentence:
            for word in listwords:
                avg += 1
        avg = avg / len(content)
        for i in range(len(wordssentence)):
            if len(wordssentence[i]) > morewords:
                morewords = len(wordssentence[i])
        for i in range(len(wordssentence)-1):
            if len(wordssentence[i])<fewerwords:
                fewerwords = len(wordssentence[i])
        tupla = (avg, morewords, fewerwords)
        return tupla
        
        
