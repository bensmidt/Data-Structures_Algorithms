from src import SglLinkLs as Link

class Solution(object):
    
    def sortList (self, head): 
        # list isn't longer than 1 element, trivially sorted
        if (head == None) or (head.next == None): 
            return head
        # split linked list
        mid = self.split_mid(head)
        # sort each linked list and merge
        right = self.sortList(mid)
        left = self.sortList(head)
        return self.merge(left, right)

    def split_mid (self, head): 
        # use a "runner" to find middle node
        slow, fast = head, head
        while (fast.next != None) and (fast.next.next != None): 
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        # detach tail of head to creat two linked lists
        slow.next = None
        return mid

    def merge (self, l_head, r_head): 
        # use dummy as beginning of sorted list
        dummy = tail = Link.Node(None)
        while (l_head != None) and (r_head != None): 
            # next value is l_head
            if l_head.val < r_head.val: 
                tail.next = l_head
                tail = tail.next
                l_head = l_head.next
            # next value is r_head
            else: 
                tail.next = r_head
                tail = tail.next
                r_head = r_head.next
        # one of these evaluate to None --> other node will be attached to tail
        tail.next = l_head or r_head
        # skip the dummy value
        return dummy.next

    def print(self, node): 
        cur = node
        while cur != None: 
            print(cur.val)
            cur = cur.next
        return

def main(): 
    Sol = Solution()

    link_ls = Link.LinkedList()
    link_ls.insert_list([4,2,1,3])
    link_ls.head = Sol.sortList(link_ls.head)
    assert link_ls.array() == [1, 2, 3, 4]

    link_ls = Link.LinkedList()
    link_ls.insert_list([4])
    link_ls.head = Sol.sortList(link_ls.head)
    assert link_ls.array() == [4]
    
    link_ls = Link.LinkedList()
    link_ls.insert_list([2,1])
    link_ls.head = Sol.sortList(link_ls.head)
    assert link_ls.array() == [1, 2]

    link_ls = Link.LinkedList()
    link_ls.insert_list([23, 4, 6, 7, 3, 2, 34, 3, 4, 46, 3, 23, 546, 6])
    link_ls.head = Sol.sortList(link_ls.head)
    assert link_ls.array() == [2, 3, 3, 3, 4, 4, 6, 6, 7, 23, 23, 34, 46, 546]

    link_ls = Link.LinkedList()
    link_ls.insert_list([10, 3, 34, 34, 21, 67, 98, 9, 45, 34, 23, 72, 84])
    link_ls.head = Sol.sortList(link_ls.head)
    assert link_ls.array() == [3, 9, 10, 21, 23, 34, 34, 34, 45, 67, 72, 84, 98]

    print ("All Test Cases Passed!")


if __name__ == "__main__": 
    main()
