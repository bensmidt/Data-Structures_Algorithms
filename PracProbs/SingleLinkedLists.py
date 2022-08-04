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

    def __str__ (self): 
        cur = self.head
        link_list_str = ''

        # check list isn't empty
        if cur == None: 
            return link_list_str

        # add items to string
        while cur.next != None: 
            link_list_str += str(cur.val) + '\n'
            cur = cur.next
        link_list_str += str(cur.val)

        return link_list_str

def main():
    ls = LinkedList()
    duplicates = [4, 5, 2, 3, 5, 4, 2, 3, 5, 3, 3, 3, 5, 7, 8, 5, 3, 4, 6, 6, 4, 45, 2]

    for i in range(len(duplicates)): 
        ls.insert_first(duplicates[i])

    ls.remove_dups_hash()
    
    print(ls)


if __name__ == "__main__": 
    main()
    