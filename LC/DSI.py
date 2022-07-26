# Author: Benjamin Smidt
# Date Created: June 2, 2022
# Topic: Data Structure I Questions and Answers


class Solution(object):
    
    # Created: June 2, 2022
    # Last Edited: June 2, 2022
    '''
    QUESTION 1 (LC 217): Contains Duplicate
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.
    '''
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not (len(nums) == len(set(nums)))
    '''
    SOLVED: check if the length of the set of the list equals length of the list. If so, no duplicate exists
    '''


    # Created: June 2, 2022
    # Last Edited: June 2, 2022
    '''
    QUESTION 2 (LC 53): Maximum Subarray
    Given an integer array nums, find the contiguous subarray (containing at least one number) 
    which has the largest sum and return its sum.
    A subarray is a contiguous part of an array.
    '''
    def maxSubArray_bf(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0): 
            return None
        
        max_sum = nums[0]
        for i in range(len(nums)): 
            for j in range(i+1, len(nums)+1): 
                temp_sum = sum(nums[i:j])
                max_sum = max(max_sum, temp_sum)

        return max_sum

    def maxSubArray_dp(self, nums): 
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        dp.append(nums[0])
        current_largest_sum = dp[0]
        for i in range(1, len(nums)):
            dp.append(max(dp[i-1] + nums[i], nums[i]))
            if dp[i] > current_largest_sum:
                current_largest_sum = dp[i]

        print(dp)
        return current_largest_sum

    '''
    SOLVED: 
        1) Use brute force and check all possible arrays; this is O(N^2), highly inefficient
        2) Use dynamic programming: https://medium.com/tech-life-fun/leet-code-53-maximum-subarray-detailed-explained-python3-solution-d91c7affc02a

    '''

def main(): 
    sols = Solution()

    #1
    assert (sols.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True)
    assert (sols.containsDuplicate([1,2,3,4]) == False)

    #2
    # brute force
    assert (sols.maxSubArray_bf([-2,1,-3,4,-1,2,1,-5,4]) == 6)
    assert (sols.maxSubArray_bf([1]) == 1)
    assert (sols.maxSubArray_bf([5,4,-1,7,8]) == 23)

    # dynamic programming
    assert (sols.maxSubArray_dp([-2,1,-3,4,-1,2,1,-5,4]) == 6)
    assert (sols.maxSubArray_dp([1]) == 1)
    assert (sols.maxSubArray_dp([5,4,-1,7,8]) == 23)


    print("Solutions Complete")

if __name__ == '__main__': 
    main()