from cmath import inf

# Introduction to Algorithms (Chapter 2? Chapter 3? Idk)

class Solution (object): 
    '''PSUEDOCODE

    FIND-MAX-CROSSING-SUBARRAY (A, low, mid, high):
        left-sum = -inf
        sum = 0
        for (i = mid) downto low: 
            sum = sum + A[i]
            if (sum > left-sum): 
                left-sum = sum
                max-left = i
        
        right-sum = -inf
        sum = 0
        for (j = mid+1) to high: 
            sum = sum + A[j]
            if (sum > right-sum): 
                right-sum = sum
                max-right = j
        
        return (max-left, max-right, left-sum+right-sum)

    FIND-MAX-SUBARRAY (A, low, high): 
        if (low == high): 
            return (low, high, A[low])
        else: 
            mid = (low + high) // 2
            left_low, left_high, left_sum = FIND-MAX-SUBARRAY (A, low, mid)
            right_low, right_high, right_sum = FIND-MAX-SUBARRAY (A, mid+1, high)
            cross_low, cross_high, cross_sum = FIND-MAX-CROSSING-SUBARRAY (A, low, mid, high)

            max_sum = max(left_sum, right_sum, cross_sum)
            if max_sum == left_sum: 
                return left_low, left_high, left_sum
            elseif max_sum == right_sum: 
                return right_low, right_high, right_sum
            else: 
                return cross_low, cross_high, cross_sum
    '''

    def find_max_crossing_subarray(self, A, low, mid, high): 
        """
        returns the maximum subarray between two continous subarrays in a list of integers

        :type A: List[int]
        :type low: int
        :type mid: int
        :type high: intm

        :rtype max_left: int
        :rtype max_right: int
        :rtype left_sum+right_sum: int
        """
        left_sum = -inf
        sum = 0
        for i in range(mid, low-1, -1): 
            sum = sum + A[i]
            if (sum > left_sum): 
                left_sum = sum
                max_left = i

        right_sum = -inf
        sum = 0
        for j in range(mid+1, high+1): 
            sum = sum + A[j]
            if (sum > right_sum): 
                right_sum = sum
                max_right = j 

        return (max_left, max_right, left_sum+right_sum)

    def find_max_subarray (self, A, low, high, call_num): 
        """
        returns the maximum subarray from a list of integers
        :type A: List[int]
        :type low: int
        :type high: int

        :rtype array_low: int
        :rtype array_high: int
        :rtype array_sum: int

        """

        if (low == high): 
            return low, high, A[low]
        else: 
            mid = (low + high) // 2
            left_low, left_high, left_sum = self.find_max_subarray (A, low, mid, call_num+1)
            right_low, right_high, right_sum = self.find_max_subarray (A, mid+1, high, call_num+1)
            cross_low, cross_high, cross_sum = self.find_max_crossing_subarray (A, low, mid, high)

            max_sum = max(left_sum, right_sum, cross_sum)
            if max_sum == left_sum: 
                return left_low, left_high, left_sum
            elif max_sum == right_sum: 
                return right_low, right_high, right_sum
            else: 
                return cross_low, cross_high, cross_sum


def main(): 
    Sol = Solution()

    A1 = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    A2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    A3 = [1]
    A4 = [5, 4, -1, 7, 8]

    assert Sol.find_max_subarray(A1, 0, len(A1)-1, 1) == (7, 10, 43)
    assert Sol.find_max_subarray(A2, 0, len(A2)-1, 1)[2] == 6
    assert Sol.find_max_subarray(A3, 0, len(A3)-1, 1)[2] == 1
    assert Sol.find_max_subarray(A4, 0, len(A4)-1, 1)[2] == 23

    print("All Test Cases Passed!")

if __name__ == "__main__": 
    main()