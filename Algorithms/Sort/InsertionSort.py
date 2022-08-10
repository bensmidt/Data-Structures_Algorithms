# Programmer: Benjamin Smidt
# Purpose: Notes and Problems on Insertion Sort
# Created: June 15, 2022
# Last Edited: June 20, 2022

# Reference: Introduction to Algorithms

"""
COMPLEXITY: O(N^2)

DESCRIPTION:  Insertion sort works the way many people sort a hand of
playing cards. We start with an empty left hand and the cards face down on the
table. We then remove one card at a time from the table and insert it into the
correct position in the left hand. To find the correct position for a card, we compare
it with each of the cards already in the hand, from right to left, as illustrated in
Figure 2.1. At all times, the cards held in the left hand are sorted, and these cards
were originally the top cards of the pile on the table

EFFICIENT FOR: Small number of elements

PSUEDOCODE: 

A = array of random numbers 

for (j = 2) to A.length
    key = A[j]
    // Insert A[j] into the sorted sequence A[1..j-1]
    i = j - 1
    while (i > 0) and A[i] > key
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key

"""

class InsertionSort (object): 
    def non_dcr (self, nums): 
        for j in range(1, len(nums)): 
            cur = nums[j]
            i = j - 1
            while (i >= 0) and (nums[i] > cur): 
                nums[i + 1] = nums[i]
                i -= 1
            nums[i + 1] = cur
        return
    
    def non_inc (self, nums): 
        for j in range(1, len(nums)): 
            cur = nums[j]
            i = j - 1
            while (i >= 0) and (nums[i] < cur): 
                nums[i + 1] = nums[i]
                i -= 1
            nums[i + 1] = cur
        return



def main(): 
    Sort = InsertionSort()

    # Test non-decreasing function
    nums = [31, 41, 59, 26, 41, 58]
    Sort.non_dcr(nums)
    assert (nums == [26, 31, 41, 41, 58, 59])


    # Test non-increasing function
    Sort.non_inc(nums)
    assert (nums == [59, 58, 41, 41, 31, 26])
    print("Test Cases Passed!")

if __name__ == "__main__": 
    main()

"""
INTERESTING THINGS: 

1. Improving Insertion Sort with Binary Search
    The while loop of lines 5 - 7 of procedure INSERTION-SORT scans backward
    through the sorted array A[1...j-1] to find the appropriate place for A[j]. The
    hitch is that the loop not only searches for the proper place for A[j], but that it also
    moves each of the array elements that are bigger than A[j] one position to the right
    (line 6). These movements can take as much as O(j) time, which occurs when all
    the j - 1 elements preceding A[j] are larger than A[j]. We can use binary search
    to improve the running time of the search to O(log(j)), but binary search wil have no
    effect on the running time of moving the elements. Therefore binary search alone cannot
    improve the worst-case running time of Insertion-Sort to O(Nlog(N))

"""