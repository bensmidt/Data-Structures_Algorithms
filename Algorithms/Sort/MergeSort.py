# Programmer: Benjamin Smidt
# Purpose: Notes and Problems on Merge Sort
# Created: June 20, 2022
# Last Edited: June 20, 2022

# Reference: Introduction to Algorithms (pg. 30 of the book; 51 of the pdf)

"""
COMPLEXITY: O(Nlog(N))

DESCRIPTION:  The merge sort algorithm closely follows the divide-and-conquer paradigm. 
Intuitively, it operates as follows:

Divide: Divide the n-element sequence to be sorted into two subsequences of n=2 elements each.
Conquer: Sort the two subsequences recursively using merge sort.
Combine: Merge the two sorted subsequences to produce the sorted answer.

The recursion “bottoms out” when the sequence to be sorted has length 1, in which
case there is no work to be done, since every sequence of length 1 is already in
sorted order.

The key operation of the merge sort algorithm is the merging of two sorted
sequences in the “combine” step. We merge by calling an auxiliary procedure
MERGE(A, p, a, r), where A is an array and p, q, and r are indices into the array
such that p <= q < r. The procedure assumes that the subarrays A[p..q] and
A[q + 1..r] are in sorted order. It merges them to form a single sorted subarray
that replaces the current subarray A[p..r].

Our MERGE procedure takes time O(n), where n = r - p + 1 is the total
number of elements being merged, and it works as follows. Returning to our card-playing 
motif, suppose we have two piles of cards face up on a table. Each pile is
sorted, with the smallest cards on top. We wish to merge the two piles into a single
sorted output pile, which is to be face down on the table. Our basic step consists
of choosing the smaller of the two cards on top of the face-up piles, removing it
from its pile (which exposes a new top card), and placing this card face down onto
the output pile. We repeat this step until one input pile is empty, at which time
we just take the remaining input pile and place it face down onto the output pile.
Computationally, each basic step takes constant time, since we are comparing just
the two top cards. Since we perform at most n basic steps, merging takes O(n)
time.

The following pseudocode implements the above idea, but with an additional
twist that avoids having to check whether either pile is empty in each basic step.
We place on the bottom of each pile a sentinel card, which contains a special value
that we use to simplify our code. Here, we use infinity as the sentinel value, so that
whenever a card with 1 is exposed, it cannot be the smaller card unless both piles
have their sentinel cards exposed. But once that happens, all the nonsentinel cards
have already been placed onto the output pile. Since we know in advance that
exactly r - p + 1 cards will be placed onto the output pile, we can stop once we
have performed that many basic steps.

PSUEDOCODE: (merge function the merge sort)

MERGE(A, p, q, r)
    n1 = q - p + 1 # length of A[p..q]
    n2 = r - q # length of A[(q + 1)..r]
    # +1's are to hold sentinels
    let L[1..(n1 + 1)] and R[1..(n2 + 1)] be new arrays 
    # copy arrays into L and R
    for (i = 1) to n1: 
        L[i] = A[p + i - 1]
    for (j = 1) to n2: 
        R[j] = A[q + j]
    # add sentinel values
    L[n1 + 1] = inf
    R[n2 + 1] = inf
    i = 1
    j = 1
    for (k = p) to r: 
        if L[i] <= R[j]: 
            A[k] = L[i]
            i = i + 1
        else A[k] = R[j]: 
            j = j + 1

MERGE-SORT(A, p, r)
    # if p >= r, subarray has at most one elements --> alr sorted
    if (p < r): 
        q = [(p + r)/2]
        MERGE-SORT(A, p, q)
        MERGE-SORT(A, q + 1, r)
        MERGE(A, p, q, r)

"""

from cmath import inf


class MergeSort(object): 
     
    def non_inc_merge(self, A, p, q, r): 
        # get lengths of left and right arrays
        left_array_len = q - p
        right_array_len = r - q

        # define left and right arrays
        left = []
        for i in range(left_array_len): 
            left.append(A[p + i])
        right = []
        for i in range(right_array_len): 
            right.append(A[q + i])
        
        # add infinities
        left.append(-inf)
        right.append(-inf)

        l_idx = 0
        r_idx = 0
        for i in range(r-p): 
            if (left[l_idx] >= right[r_idx]):
                A[p+i] = left[l_idx]
                l_idx += 1
            else: 
                A[p+i] = right[r_idx]
                r_idx += 1
                
        return

    def non_inc(self, A, p, r): 
        if p < r: 
            q = (p + r)//2
            self.non_inc(A, p, q)
            self.non_inc(A, q+1, r)
            self.non_inc_merge(A, p, q, r)
        return
    


def main(): 
    Sort = MergeSort()

    # Test non-decreasing function
    nums = [31, 59, 26, 58, 41, 41]
    length = len(nums)
    Sort.non_inc(nums, 0, length)
    assert (nums == [59, 58, 41, 41, 31, 26])


    # Test non-increasing function
    '''
    Sort.non_inc(nums)
    assert (nums == [26, 31, 41, 41, 58, 59])
    '''
    print("Test Cases Passed!")

if __name__ == "__main__": 
    main()