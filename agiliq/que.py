
"""
push and pop operations using class 
"""
__author__ = '__Mani__'

class Queue(object):
    def __init__(self):
        self.Queue = []
    

    def push(self,obj):
        self.Queue.append(obj)
        
        

    def pop(self):
        return self.Queue.pop()

        


def main():
    my_queue = Queue()
    my_queue.push(5)
    my_queue.push(4)

    print (my_queue.pop())
    print (my_queue.pop())


if __name__ == '__main__':
    main()
