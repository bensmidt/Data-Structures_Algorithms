# Programmer: Benjamin Smidt
# Purpose: Quick Sort
# Created: July 19, 2022
# Last Edited: July 20, 2022

# Reference: Introduction to Algorithms (Chapter 7)

'''
PSUEDOCODE for 

A: array 
p: index < r
r: index > p

PARTITION(A, p, r):
    x = A[r]
    i = p - 1
    j = p 
    while j <= r: 
        if A[j] <= x:
            i = i + 1
            exchange A[i] with A[j]
    echange A[i+1] with A[r]
    return i + 1

QUICKSORT (A, p, r)
if p < r
    q = PARTITION (A, p, r)
    QUICKSORT (A, p, q-1)
    QUICKSORT (A, q+1, r)
'''

class QuickSort(object): 

    def partition (self, A, p, r): 
        x = A[r]
        i = p - 1
        j = p
        while (j < r): 
            if A[j] <= x: 
                i = i + 1
                j_val = A[j]
                A[j] = A[i]
                A[i] = j_val
            j = j + 1
        print('i =', i)
        print('r =', r)
        r_val = A[r]
        A[r] = A[i + 1]
        A[i + 1] = r_val
        return i + 1

    def quicksort (self, A, p, r): 
        if (p < r): 
            q = self.partition (A, p, r)
            print('q =', q)
            print(A)
            self.quicksort (A, p, q-1)
            self.quicksort (A, q+1, r)
        return

def main(): 
    Sort = QuickSort()

    # Quicksort
    A = [31, 41, 59, 26, 41, 58]
    Sort.quicksort(A, 0, len(A)-1)
    print(A)

if __name__ == "__main__": 
    main()
