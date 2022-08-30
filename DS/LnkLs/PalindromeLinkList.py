from src.SglLinkLs import Node, LinkedList

class Solution (object): 

    """https://leetcode.com/problems/palindrome-linked-list/submissions/"""

    # TIME COMPLEXITY: O(N)
    # SPACE COMPLEXITY: O(1)
    def is_palindrome(self, head: Node) -> bool: 
        """Returns a bool indicating whether the linked list is a palindrome or not
        Inputs: 
        - head: head of a linked list; type: Node
        Returns: 
        - is_pal: bool indicating if linked list is a palindrome
        """

        # empty
        if head == None: 
            return False
        # trivial case
        if head.next == None: 
            return True
        if head.next.next == None: 
            return head.val == head.next.val

        # split linked list into two linked lists
        cur = head
        runner = head.next.next
        
        while True: 
            # reached end, odd number of values
            if runner.next == None: 
                # break off middle from linked list
                mid = cur.next
                cur.next = None
                # start new linked list at the node after middle
                head_two = mid.next
                mid.next == None
                break

            # reached end, even number of values
            elif runner.next.next == None: 
                runner = runner.next
                cur = cur.next
                # break list in half
                head_two = cur.next
                cur.next = None
                break
            
            runner = runner.next.next
            cur = cur.next
        
        # reverse second list
        two_behind = None
        prev = None
        cur = head_two

        while cur.next != None: 
            # move all three nodes
            two_behind = prev
            prev = cur
            cur = cur.next
            # turn previous to point to 2 behind
            prev.next = two_behind
        
        cur.next = prev
        head_two = cur

        # check if lists are the same
        cur1 = head
        cur2 = head_two
        while cur1.next != None and cur2.next != None: 
            if cur1.val != cur2.val: 
                return False
            cur1 = cur1.next
            cur2 = cur2.next

        # two linked lists are the same length, this is the last value needing to evaluate to true
        return cur1.val == cur2.val


def test(ls, ans): 
    Sol = Solution()
    lnkls = LinkedList()
    lnkls.insert_list(ls)
    is_palindrome = Sol.is_palindrome(lnkls.head)
    print("is palindrome?:", is_palindrome)
    assert is_palindrome == ans

def main(): 
    test([1], True)
    test([1, 2, 1], True)
    test([1, 5, 5, 1], True)
    test([1, 5, 6, 7], False)
    test([], False)
    test([1, 2, 3, 3, 2, 1], True)
    test([1, 2, 3, 2, 1], True)

if __name__ == "__main__": 
    main()




            


            
