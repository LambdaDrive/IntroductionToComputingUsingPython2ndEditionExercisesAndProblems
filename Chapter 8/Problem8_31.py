import time
class Date:

    def __init__(self):

        self.data = time.localtime()

    def display(self, forma):
        if forma == 'MDY':
            print('{}/{}/{}'.format(time.strftime('%m',self.data),time.strftime('%d',self.data),time.strftime('%y',self.data)))
        elif forma == 'MDYY':
            print('{}/{}/{}'.format(time.strftime('%m',self.data),time.strftime('%d',self.data),time.strftime('%Y',self.data)))
        elif forma == 'DMY':
            print('{}/{}/{}'.format(time.strftime('%d',self.data),time.strftime('%m',self.data),time.strftime('%y',self.data)))    
        elif forma == 'DMYY':
            print('{}/{}/{}'.format(time.strftime('%d',self.data),time.strftime('%m',self.data),time.strftime('%Y',self.data)))
        elif forma == 'MODY':
            print('{} {}, {}'.format(time.strftime('%b', self.data), time.strftime('%d', self.data), time.strftime('%Y', self.data)))

        
