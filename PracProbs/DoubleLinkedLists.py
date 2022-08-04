
class Node (object): 
    def __init__ (self, val, prev, next): 
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList (object): 
    def __init__ (self, head, tail): 
        head.next = tail
        tail.prev = head
        self.head = head
        self.tail = tail
        
