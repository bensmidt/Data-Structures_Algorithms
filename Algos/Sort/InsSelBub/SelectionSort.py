# Programmer: Benjamin Smidt
# Purpose: Notes and Problems on Insertion Sort
# Created: June 15, 2022
# Last Edited: June 17, 2022

# Reference: Introduction to Algorithms

"""
COMPLEXITY: O(N^2)

DESCRIPTION: 

PSUEDOCODE: 

A = array of random numbers 

for (j = 1) to (A.length - 1)
    smallest = j
    for (i = j+1) to A.length):
        cur = A[i]
        if (A[i] < A[smallest]): 
            smallest = i
     exchange A[j] with A[smallest]

"""

class SelectionSort (object): 
    def non_dcr (self, nums): 
        for j in range(0, len(nums) - 1): 
            min_idx = j
            for i in range(j+1, len(nums)): 
                if (nums[i] < nums[min_idx]): 
                    min_idx = i
            min = nums[min_idx]
            nums[min_idx] = nums[j]
            nums[j] = min
        return
    
    def non_inc (self, nums): 
        pass



def main(): 
    Sort = SelectionSort()

    # Test non-decreasing function
    nums = [31, 41, 59, 26, 41, 58]
    Sort.non_dcr(nums)
    assert (nums == [26, 31, 41, 41, 58, 59])


    # Test non-increasing function
    Sort.non_inc(nums)
    # assert (nums == [59, 58, 41, 41, 31, 26])


    print("Test Cases Passed!")

if __name__ == "__main__": 
    main()