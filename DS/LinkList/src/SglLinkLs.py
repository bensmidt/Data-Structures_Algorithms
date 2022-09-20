class Node(object): 
    def __init__ (self, val, next = None): 
        self.val = val 
        self.next = next

class LinkedList(object): 
    def __init__ (self): 
        self.head = None

    def insert_first (self, val): 
        new_link = Node(val)
        
        new_link.next = self.head
        self.head = new_link
        return

    def insert_list (self, ls): 
        """Creates a linked list from a list of integers
        :type: ls: List
        """
        # check list isn't empty
        if len(ls) == 0: 
            return
        
        # define head
        self.head = Node(val = ls.pop())

        # create links
        for i in range(len(ls)): 
            self.insert_first(ls.pop())

        return

    def array(self): 
        cur = self.head
        link_list = []

        # check list isn't empty
        if cur == None: 
            return link_list

        # add items to string
        while cur.next != None: 
            link_list.append(cur.val)
            cur = cur.next
        link_list.append(cur.val)

        return link_list

    def __str__ (self): 
        cur = self.head
        link_list_str = ''

        # check list isn't empty
        if cur == None: 
            return link_list_str

        # add items to string
        while cur.next != None: 
            link_list_str += str(cur.val) + ', '
            cur = cur.next
        link_list_str += str(cur.val)

        return link_list_str


def main():
    pass


if __name__ == "__main__": 
    main()
    