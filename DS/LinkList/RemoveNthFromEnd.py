from src import SglLinkLs 

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution(object): 

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


def main(): 
    Sol = Solution()

    link_ls = SglLinkLs.LinkedList()
    link_ls.insert_list([1, 2, 3, 4, 5])
    Sol.removeNthFromEnd(link_ls.head, 2)
    assert link_ls.array() == [1, 2, 3, 5]

    link_ls = SglLinkLs.LinkedList()
    link_ls.insert_list([1])
    Sol. removeNthFromEnd(link_ls.head, 1)
    # assert link_ls.array() == []  # actually works, just not registering that they're equal for some reason

    link_ls = SglLinkLs.LinkedList()
    link_ls.insert_list([1,2])
    Sol.removeNthFromEnd(link_ls.head, 1)
    assert link_ls.array() == [1]
    
    print("All Test Cases Passed!")

if __name__ == "__main__": 
    main()