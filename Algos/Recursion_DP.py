from cmath import inf
from random import randint

class RecDP (object): 
    #1 Divide-And-Conquer
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
    
    #2 Dynamic Programming
    def triple_step (self, n): 
        """Calculates possible ways to climb stairs with n steps given you can take 1, 2, or 3 steps
        Args: 
            n (int): number of steps in the stairs
            returns (int): number of possible ways to climb up the stairs
        """

        # define first four steps with 0 being zero stairs
        posbl_steps_ls = [1, 1, 2]

        # use dp to grap rest of steps
        i = 3
        while i <= n: 
            # define options if taken steps from previous steps
            one_step = i - 1
            two_step = i - 2
            three_step = i - 3

            cur_posbl_steps = posbl_steps_ls[one_step] + posbl_steps_ls[two_step] + posbl_steps_ls[three_step]
            posbl_steps_ls.append(cur_posbl_steps)
            i += 1

        return posbl_steps_ls[n]

    #3 Dynamic Programming w/ Recursion
    def triple_step_helper (self, n, memo): 
        if (n < 0): 
            return 0
        elif (n == 0): 
            return 1
        elif memo[n-1] > -1: 
            return memo[n-1]
        else: 
            memo[n-1] = self.triple_step_helper(n-1, memo) + self.triple_step_helper(n-2, memo) + self.triple_step_helper(n-3, memo)
            return memo[n-1]
    
    def triple_step_rec (self, n): 
        """Calculates possible ways to climb stairs with n steps given you can take 3 steps (using recursion)
        Args: 
            n (int): number of steps in the stairs
            returns (int): number of possible ways to climb up the stairs
        """
        posbl_steps_ls = []
        for i in range(n): 
            posbl_steps_ls.append(-1)

        return self.triple_step_helper(n, posbl_steps_ls)

    #4 Recursion w/ Backtracking
    class Queens (object):
        def __init__ (self, n = 8):
            self.board = []
            self.n = n
            for i in range (self.n):
                row = []
                for j in range (self.n):
                    row.append ('*')
                self.board.append (row)

        # print the board
        def print_board (self):
            for i in range (self.n):
                for j in range (self.n):
                    print (self.board[i][j], end = ' ')
                print ()
            print ()

        # check if a position on the board is valid
        def is_valid (self, row, col):
            for i in range (self.n):
                if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
                    return False
            for i in range (self.n):
                for j in range (self.n):
                    row_diff = abs (row - i)
                    col_diff = abs (col - j)
                    if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                        return False
            return True
            
        # do the recursive backtracking
        def recursive_solve (self, col, solns):
            if (col == self.n):
                solns.append(self.board)
            else:
                for i in range (self.n):
                    if (self.is_valid (i, col)):
                        self.board[i][col] = 'Q'
                        if (self.recursive_solve(col + 1, solns)):
                            return True
                        self.board[i][col] = '*'
                return False

        # if the problem has a solution print the board
        def solve (self):
            solns = []
            self.recursive_solve (0, solns)
            soln_count = len(solns)
            return soln_count
        
    #5 Recursion w/ Backtracking
    def robot_grid (self, matrix):     
        """Calculate a valid path for a robot to travel through a matrix
        """
        pass

class Test (object): 
    # Test #1: Max Subarray
    def find_max_subarray (self): 
        A1 = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        A2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        A3 = [1]
        A4 = [5, 4, -1, 7, 8]
        SA_Test = RecDP()
    
        assert SA_Test.find_max_subarray(A1, 0, len(A1)-1, 1) == (7, 10, 43)
        assert SA_Test.find_max_subarray(A2, 0, len(A2)-1, 1)[2] == 6
        assert SA_Test.find_max_subarray(A3, 0, len(A3)-1, 1)[2] == 1
        assert SA_Test.find_max_subarray(A4, 0, len(A4)-1, 1)[2] == 23

        print("All 4 find_max_subarrary Test Cases Passed!")

    # Test #4: Eight Queens
    def eight_queens (self, num_cases): 
        # eight queens answers
        ans = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200]

        # tests
        for i in range(1, num_cases+1): 
            queen_test = RecDP.Queens(i)
            assert queen_test.solve() == ans[i]
        
        print("All {} eight_queens Test Cases passed!".format(i))

def main(): 
    test = Test()

    # test.find_max_subarray()  # Test 1: Max Subarray
    # test.eight_queens(num_cases = 8)  # Test 4: Eight Queens

if __name__ == "__main__": 
    main()
