
class Sort (object): 

     def sorted_merge (self, nums1, m, nums2, n): 
        """
        Adds the sorted numbers from nums2 into nums1 to make one large sorted array
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        while (m > 0) and (n > 0): 
          if nums1[m-1] >= nums2[n-1]: 
            nums1[m+n-1] = nums1[m-1]
            m -= 1
          else: 
            nums1[m+n-1] = nums2[n-1]
            n -= 1
            
        if (n > 0): 
          nums1[:n] = nums2[:n]
        
        return nums1

def main(): 
    sort = Sort()
    
    assert sort.sorted_merge([], 0, [], 0) == []
    assert sort.sorted_merge([0], 1, [], 0) == [0]
    assert sort.sorted_merge([0], 0, [1], 1) == [1]
    assert sort.sorted_merge([0, 1, 3, 6, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0], 7, [4, 5, 6, 7, 8, 9, 10, 56, 56], 9) == [0, 1, 3, 4, 5, 6, 6, 7, 8, 8, 9, 9, 10, 10, 56, 56]
    print("All Test Cases Passed!")


if __name__ == "__main__": 
    main()