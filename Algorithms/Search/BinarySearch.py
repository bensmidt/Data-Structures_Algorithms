# Programmer: Benjamin Smidt
# Purpose: Notes and Problems on Merge Sort
# Created: June 23, 2022
# Last Edited: June 23, 2022

# Reference: Introduction to Algorithms (pg. 29 of instructor manual pdf)

"""
COMPLEXITY: O(log(N))

PSUEDOCODE: 

Iterative-Binary-Search(A, v, low, high):
    while (low <= high): 
        mid = [(low + high)]/2]
        if (v == A[mid]): 
            return mid
        elseif (v > A[mid]): 
            low = mid + 1
        else: 
            high = mid - 1
        return

Recursive-Binary-Search(A, v, low, high): 
    if (low > high): 
        return
    mid = [(low + high)/2]
    if (v == A[mid]): 
        return mid
    elseif (v > A[mid]): 
        return Recursive-Binary-Search(A, v, mid+1, high)
    else: 
        return Recursive-Binary-Search(A, v, low, mid-1)

"""
