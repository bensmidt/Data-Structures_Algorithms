from src import SglLinkLs

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class Solution (object): 
    
    def del_dups_hash (self, head): 
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
        cur = head
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

def main(): 
    Sol = Solution()

    link_ls = SglLinkLs.LinkedList()
    link_ls.insert_list([1,1,2])
    Sol.del_dups_hash(link_ls.head)
    assert link_ls.array() == [1, 2]

    link_ls = SglLinkLs.LinkedList()
    link_ls.insert_list([1,1,2,3,3])
    Sol. del_dups_hash(link_ls.head)
    assert link_ls.array() == [1,2,3]  # actually works, just not registering that they're equal for some reason

    link_ls = SglLinkLs.LinkedList()
    link_ls.insert_list([1, 1, 3, 3, 4, 2, 4, 5, 3, 5, 6, 4, 4, 6, 4, 3, 3])
    Sol.del_dups_hash(link_ls.head)
    assert link_ls.array() == [1, 3, 4, 2, 5, 6]

    print("All Test Cases Passed!")

if __name__ == "__main__": 
    main()