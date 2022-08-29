from src.SglLinkLs import Node, LinkedList

class Solution (object): 
    def is_palindrome(self, head: Node) -> bool: 
        """Returns a bool indicating whether the linked list is a palindrome or not
        Inputs: 
        - head: head of a linked list; type: Node
        Returns: 
        - is_pal: bool indicating if linked list is a palindrome"""
        # empty
        if head == None: 
            return False
        # trivial case
        if head.next == None: 
            return True
        if head.next.next == None: 
            return head.val == head.next.val

        cur = head
        runner = head.next.next
        
        while True: 
            # reached end, odd number of values
            if runner.next == None: 
                # break off middle from linked list
                mid = cur.next
                cur.next = None
                # start new linked list at the node after middle
                next = mid.next
                mid.next == None
                head_two = next
                break
            # reached end, even number of values
            elif runner.next.next == None: 
                runner = runner.next
                cur = cur.next
                # break list in half
                head_two = cur.next
                cur.next = None

            runner = runner.next.next
            cur = cur.next

        prev = None
        cur = head_two

        while cur.next != None: 
            prev = cur
            cur = cur.next

            


            
