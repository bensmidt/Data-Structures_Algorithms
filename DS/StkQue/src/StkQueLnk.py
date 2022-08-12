
class Node(object): 
    def __init__ (self, data = None, next = None, min = None): 
        self.data = data
        self.next = next

class Stack(object): 
    def __init__ (self, top = None): 
        self.top = top

    # check if stack is empty 
    def isEmpty (self): 
        return self.top == None

    # return value on top of stack 
    def peek (self): 
        # check if stack is empty
        if self.isEmpty() == True: 
            return None
        return self.top.data

    # return and take value off top of stack
    def pop (self): 
        # check if stack is empty
        if self.isEmpty() == True:
            return "Error: stack underflow"

        # pop top of stack and redefine top node
        top = self.top 
        self.top = self.top.next

        # remove min from MinStack
        self.remove_min()
        return top.data

    # add a value to top of stack 
    def push (self, data): 
        old_top = self.top
        new_top = Node(data, old_top)
        new_top.next = old_top
        self.top = new_top

        # add min to MinStack
        self.add_min(new_top)
        return

class Queue(object): 
    def __init__(self, first = None, last = Node()): 
        self.first = first
        self.last = last
        self.last.next = first

    # check if queue is empty
    def isEmpty(self): 
        return self.first == None

    # check last value in queue
    def peek(self): 
        if self.isEmpty() == True: 
            return None
        
        return self.first.data

    # add new value to queue
    def add(self, data): 
        # check if queue is empty
        if self.isEmpty() == True: 
            self.first = Node(data, self.last)
            self.last.next = self.first
            return 

        old_last = self.last.next
        new_last = Node(data, self.last)

        old_last.next = new_last
        self.last.next = new_last
        return

    # remove top value from queue
    def remove(self): 
        # check if queue is empty
        if self.isEmpty() == True: 
            return "Error: queue underflow"

        # check if only one value in queue
        if self.last.next == self.first: 
            first = self.first
            self.first = None
            return first.data

        first = self.first 
        self.first = first.next
        return first.data

def queue_test(): 
    queue = Queue()

    queue.add(1)
    print(queue.peek())
    queue.add(3)
    print(queue.peek())
    print(queue.remove())
    queue.add(4)
    print(queue.remove())
    print(queue.remove())
    print(queue.remove())


def main(): 
     # queue_test()
     return
    


if __name__ == "__main__": 
    main()