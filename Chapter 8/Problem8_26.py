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
    
