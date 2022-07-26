# Author: Benjamin Smidt
# Date Created: June 2, 2022
# Topic: Algorithms Questions and Answers


class Solution(object):
    
    # Created: June 2, 2022
    # Last Edited: June 6, 2022
    '''
    QUESTION 1 (LC 704): Binary Search
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
    You must write an algorithm with O(log n) runtime complexity.
    '''
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1

        while (lo <= hi): 
            mid = (lo + hi) // 2
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else: 
                return mid
        
        return -1

    '''
    SOLVED: binary search
    '''


    # Created: June 2, 2022
    # Last Edited: June 6, 2022
    '''
    QUESTION 2 (LC 35): Search Insert Position
    Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
    You must write an algorithm with O(log n) runtime complexity.
    '''
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if (len(nums) == 0):
            return 0

        lo = 0
        hi = len(nums) - 1

        while (lo < hi): 
            mid = lo + (hi - lo) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] < target):
                lo = mid + 1
            else: 
                # nums[mid] > target
                hi = mid
          
        if (nums[lo] < target): 
            lo += 1
            hi += 1
        
        return lo
        
    '''
    SOLVED: binary search; https://leetcode.com/problems/search-insert-position/discuss/249092/Come-on-forget-the-binary-search-patterntemplate!-Try-understand-it!
    '''


    # Created: June 13, 2022
    # Last Edited: June 13, 2022
    '''
    QUESTION 3 (LC 278): First Bad Version
    You are a product manager and currently leading a team to develop a new product. Unfortunately, 
    the latest version of your product fails the quality check. Since each version is developed based 
    on the previous version, all the versions after a bad version are also bad.
    Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes 
    all the following ones to be bad.
    You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a 
    function to find the first bad version. You should minimize the number of calls to the API.
    '''
    def firstBadVersion(self, n): 
        """
        :type n: int
        :rtype: int
        """
        lo = 1
        hi = n

        while (lo < hi): 
            mid = (lo + hi) // 2
            if (isBadVersion(mid) == True):
                hi = mid
            elif (isBadVersion(mid) == False): 
                lo = mid + 1
        
        return lo
    
    # Created: June 15, 2022
    # Last Edited: June 15, 2022
    '''
    QUESTION 4 (LC 977); Squares of a Sorted Array
    Given an integer array nums sorted in non-decreasing order, return an array 
    of the squares of each number sorted in non-decreasing order.
    '''
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        



def main(): 
    sols = Solution()

    #1 Binary Search
    bin_srch_arry = [-1, 0, 3, 5, 9, 12]
    assert (sols.search(bin_srch_arry, 9) == 4)
    assert (sols.search(bin_srch_arry, 2) == -1)

    #2 Search Insert Position
    nums = [1, 3, 5, 6]
    assert (sols.searchInsert(nums, 5) == 2)
    assert (sols.searchInsert(nums, 2) == 1)
    assert (sols.searchInsert(nums, 7) == 4)
    assert (sols.searchInsert([1, 3], 0) == 0)

    print("Solutions Complete")

if __name__ == '__main__': 
    main()
