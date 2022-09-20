from src import SglLinkLs as Link


class Solution (object): 
    def oddEvenList(self, head): 
        """Returns a linked list with all odd indices at the beginning and even indices at the end
        The first node is considered odd, the second node considered even

        Inputs: 
        - head: a node being the head of a linked list
        Returns: 
        - a node which is the head of the new linked list
        """
        if head == None or head.next == None: 
            return head
        
        odd = head 
        even_head = head.next
        even = even_head

        while (even != None) and even.next != None: 
            # skip current even node
            odd.next = even.next
            # move odd forward two nodes
            odd = odd.next
            # set even to point to next even
            even.next = odd.next
            # move even to next even node
            even = even.next
        
        # set lat odd node to point to even node
        odd.next = even_head

        return head

    def oddEvenList1(self, head): 
        """Returns a linked list with all odd indices at the beginning and even indices at the end
        The first node is considered odd, the second node considered even

        Inputs: 
        - head: a node being the head of a linked list
        Returns: 
        - a node which is the head of the new linked list
        """
        if head == None or head.next == None: 
            return head
        
        prev = head 
        cur = head.next

        # create even link list; first value is dummy value
        first_even = Link.Node(None)
        cur_even = first_even

        while (cur.next != None) and (cur.next.next != None): 
            # add node to even list
            cur_even.next = cur
            cur_even = cur_even.next
            # skip unlink node from list
            prev.next = cur.next
            # skip two values
            prev = cur.next
            cur = prev.next
        
        # list ends on even
        if cur.next == None: 
            cur_even.next = cur
            # attach end of list to beginning of even list (skip first dummy node)
            prev.next = first_even.next

        # list ends on odd
        else: # cur.next.next == None
            cur_even.next = cur
            prev.next = cur.next
            # attach end of list to beginning of even list (skip first dummy node)
            cur.next.next = first_even.next
            # ensure the list ends
            cur.next = None

        return head


def main(): 
    Sol = Solution()

    link_ls = Link.LinkedList()
    link_ls.insert_list([])
    Sol.oddEvenList(link_ls.head)
    assert link_ls.array() == []

    link_ls = Link.LinkedList()
    link_ls.insert_list([1])
    Sol.oddEvenList(link_ls.head)
    assert link_ls.array() == [1]

    link_ls = Link.LinkedList()
    link_ls.insert_list([1, 2])
    Sol.oddEvenList(link_ls.head)
    assert link_ls.array() == [1, 2]

    link_ls = Link.LinkedList()
    link_ls.insert_list([1, 2, 3])
    Sol.oddEvenList(link_ls.head)
    assert link_ls.array() == [1, 3, 2]

    link_ls = Link.LinkedList()
    link_ls.insert_list([1, 2, 3, 4])
    Sol.oddEvenList(link_ls.head)
    assert link_ls.array() == [1, 3, 2, 4]

    link_ls = Link.LinkedList()
    link_ls.insert_list([1, 2, 3, 4, 5])
    Sol.oddEvenList(link_ls.head)
    assert link_ls.array() == [1, 3, 5, 2, 4]

    link_ls = Link.LinkedList()
    link_ls.insert_list([1, 2, 3, 4, 5, 6])
    Sol.oddEvenList(link_ls.head)
    assert link_ls.array() == [1, 3, 5, 2, 4, 6]

    print("All Test Cases Passes!")


if __name__ == "__main__": 
    main()
