
# Introduction to Algorithms
# IN PROGRESS, HAVEN'T FINISHED

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
    pass

if __name__ == "__main__": 
    main()