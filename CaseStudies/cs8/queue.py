class EmptyQueueError(Exception):
    pass

class Queue:
    'a classic queue class'

    def __init__(self):
        'instantiates an empty list'
        self.q = []

    def isEmpty(self):
        'returns True if queue is empty, False otherwise'
        return (len(self.q) == 0)

    def enqueue (self, item):
        'insert item at rear of queue'
        return self.q.append(item)

#    def dequeue(self):
#        'remove and return item at front of queue'
#        return self.q.pop(0)

#   Added in Section 8.4
#    def __init__(self, q=None):
#        'initialize queue based on list q, default is empty queue'
#        if q == None:
#            self.q = []
#        else:
#            self.q = q

    def __eq__(self, other):
        '''return True if queues self and other contain
           the same items in the same order'''
        return self.q == other.q

    def __len__(self):
        'returns number of items in queue'
        return len(self.q)

    def __repr__(self):
        'return canonical string representation of queue'
        return 'Queue({})'.format(self.q)

#   Added in Section 8.6
    def dequeue(self):
        'remove and return item at front of queue'
        if len(self) == 0:
            raise EmptyQueueError('dequeue from empty queue')
        return self.q.pop(0)

#   Solution to Problem 8.9
#    def dequeue(self):
#        '''removes and returns item at front of the queue
#           raises KeyboardInterrupt exception if queue is empty'''
#        if len(self) == 0:
#            raise KeyboardInterrupt('dequeue from empty queue')
#
#        return self.q.pop(0)

#    Added in Case Study CS.8
    def __iter__(self):
        'returns Queue iterator'
        return QueueIterator(self)



class QueueIterator:
    'iterator for Queue container class'
    
    def __init__(self, q):
        'constructor'
        self.index = len(q)-1
        self.q = q

    def __next__(self):
        '''returns next Queue item; if no next item,
           raises StopIteration exception'''
        if self.index < 0:        # no next item
            raise StopIteration()

        # return next item
        res = self.q[self.index]
        self.index -= 1
        return res




    
##################################
# Solution to Practice Problem #
##################################


# Practice Problem CS.43
class oddList(list):
    'list with peculiar iteration loop pattern'

    def __iter__(self):
        'returns list iterator object'
        return ListIterator(self)



class ListIterator(object):
    'peculiar iterator for oddList class'

    def __init__(self, lst):
        'constructor' 
        self.lst = lst
        self.index = 0

    def __next__(self):
        'returns next oddList item'
        if self.index >= len(self.lst):
            raise StopIteration
        res = self.lst[self.index]
        self.index += 2
        return res


