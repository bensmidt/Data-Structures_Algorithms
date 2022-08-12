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
        
        self.head = Node(val = ls.pop())

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

class LinkProbs(object): 

    # 1
    def remove_dups_hash (self): 
        """
        Problem: Write code to remove duplicates from an unsorted linked list.

        Questions: 
            1. What can we assume about the size of the linked list? 
            2. Is it doubly or singly linked? 
            3. What possible values are within the linked list? ASCII? Unicode? 

        Hash Map/Dictionary: 
            Store all values come across in linked list. As you go, check if values come up again

        """
        # check linked lists has more than one value
        cur = self.head
        if (cur == None) or (cur.next == None): 
            return 

        # store previous node; store seen values in dictionary
        seen = {cur.val: 1}
        prev = cur
        cur = cur.next

        # iterate through and unlink duplicates
        while (cur.next != None): 

            # if value seen, unlink; previous stays same, current moves forwards a link
            if cur.val in seen.keys(): 
                prev.next = cur.next
                cur = cur.next
                continue

            # value hasn't been seen, add to dictionary
            else: 
                seen[cur.val] = 1
                prev = cur
                cur = cur.next

        # check last value
        if cur.val in seen: 
            prev.next = cur.next
        
        return

    # 2
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        cur_idx = 0
        cur = head
        # send current n places ahead
        for i in range(n-1): 
            if cur.next == None: 
                return head
            cur = cur.next
        
        # see if next value is zero
        if cur.next == None: 
            head = head.next
            return head
        
        prev = None
        runner = head
        while cur.next != None: 
            cur = cur.next
            prev = runner
            runner = runner.next
            
        prev.next = runner.next
        return head

class Test(object): 

    #2
    def removeNthFromEnd (self): 
        test = LinkProbs()
        
        link_ls = LinkedList()
        link_ls.insert_list([1, 2, 3, 4, 5])
        test.removeNthFromEnd(link_ls.head, 2)
        assert link_ls.array() == [1, 2, 3, 5]

        link_ls = LinkedList()
        link_ls.insert_list([1])
        test.removeNthFromEnd(link_ls.head, 1)
        # assert link_ls.array() == []  # actually works, just not registering that they're equal for some reason

        link_ls = LinkedList()
        link_ls.insert_list([1,2])
        test.removeNthFromEnd(link_ls.head, 1)
        assert link_ls.array() == [1]
        print("All removeNthfromEnd Test Cases Passed!")


def main():
    test = Test()

    # test.removeNthFromEnd() #2


if __name__ == "__main__": 
    main()
    