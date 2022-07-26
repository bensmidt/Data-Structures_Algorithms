# Programmer: Benjamin Smidt
# Purpose: Notes and Problems w/ Heap Sort
# Created: July 19, 2022
# Last Edited: July 19, 2022

# Reference: Introduction to Algorithms

# Didn't finish the priority queues and 

'''
PSUEDOCODE

MAX-HEAPIFY(A, i): 
    l = 2i  # left child node (if it exists)
    r = 2i + 1  # right child node (if it exists)
    if (l <= A.heap-size) and (A[l] > A[i]): 
        largest = l
    else: 
        largest = i
    if (r <= A.heap-size) and (A[r] > A[largest]): 
        largest = r
    if largest != i
        exchange A[i] with A[largest]
        MAX-HEAPIFY(A, largest)

COMPLEXITY: O(lg n)

BUILD-MAX-HEAP(A): 
    A.heap-size = A.length
    for i = A.length // 2 downto 1
        MAX-HEAPIFY(A, i)

COMPLEXITY: O(n)

HEAPSORT(A): 
    BUILD-MAX-HEAP(A)
    for i = A.length downto 2
        exchange A[1] with A[i]
        A.heap-size = A.heap-size - 1
        MAX-HEAPIFY(A, 1)

COMPLEXITY: O(n lg n)
'''

class Heapsort (object):
    def __init__ (self, A, heap_size = 0): 
        self.heap_size = heap_size
        self.length = len(A)
    
    def heap_size (self, heap_size): 
        self.heap_size = heap_size
    
    def right(self, i): 
        return 2*(i+1)

    def left(self, i): 
        return 2*(i+1) - 1

    def min_heapify(self, A, i): 
        # define child nodes left and right
        l = self.left(i)
        r = self.right(i)

        # find largest node between 
        if (l < self.heap_size) and (A[l] > A[i]): 
            largest = l
        else: 
            largest = i
        if (r < self.heap_size) and (A[r] > A[largest]): 
            largest = r

        # heapify if parent/children don't satisfy heap requirements
        if (largest != i): 
            idx_val = A[i]
            A[i] = A[largest]
            A[largest] = idx_val
            self.min_heapify(A, largest)

    def build_min_heap(self, A): 
        self.heap_size, self.length = len(A), len(A)
        for i in range( (len(A)//2)+1, -1, -1): 
            self.min_heapify(A, i)

    def heapsort(self, A): 
        self.build_min_heap(A)
        for i in range(len(A)-1, 0, -1): 
            first_val = A[0]
            A[0] = A[i]
            A[i] = first_val 
            self.heap_size = self.heap_size - 1
            self.min_heapify(A, 0)


class PriorityQueue(object): 
    def __init__ (self, A, heap_size): 
        self.A = A
        self.heap_size = heap_size
        self.Sort = Heapsort(self.A, self.heap_size)
        self.Sort.heapsort(self.A)

    def heap_min (self): 
        return self.A[0]

    def extract_min (self): 
        # check if heap_size is valid
        if self.heap_size < 1: 
            print("error: heap underflow")
            return None
        
        max = self.A[0]
        self.A[0] = self.A[self.heap_size]
        self.Sort.min_heapify(self.A, 0)
        return max



def main(): 
    A = [3, 5, 1, 6, 67, 23, 635, 6, 6, 82, 2]
    Sort = Heapsort(A)
    
    Sort.heapsort(A)
    print(A)

    PriQ = PriorityQueue(A, len(A)-1)
    print(PriQ.extract_min())
    print(PriQ.A)

if __name__ == "__main__": 
    main()



    