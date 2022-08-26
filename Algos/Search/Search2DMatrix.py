from random import randint

class Solution (object): 
    """https://leetcode.com/problems/search-a-2d-matrix/solution/"""

    """My initial solution used the first three functions. It is a perfectly good solution 
    (in the technical sense) holding the same time complexity O(log(mn)) and space 
    complexity O(1) as my second solution. However, it's much longer than it needs to be 
    which is bad for readability, documentation, use, etc. Overall the second solution is 
    much better and far more conise."""

    def search_matrix(self, matrix: list[list[int]], target: int) -> bool: 
        """Returns a bool indicating if target is in matrix
        Inputs: 
        - matrix: 2D array of integers
            integers in each row are sorted left to right
            first integer of each row is greater than the last integer of the previous row
        - target: integer
        Returns: 
        - in_matrix: bool that is true if target is in matrix, false otherwise
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: 
            return False
        
        srch_row = self.bin_row_srch(matrix, target)
        return self.bin_srch(matrix[srch_row], target)

    def bin_row_srch(self, matrix: list[list[int]], target: int) -> int: 
        """Returns the row index of matrix in which the target may be located
        Inputs: 
        - matrix: 2D array of integers
            integers in each row are sorted left to right
            first integer of each row is greater than the last integer of the previous row
        - target: integer
        Returns: 
        - row: int indicating the row index within matrix in which target may be located
        """
        lo = 0
        hi = len(matrix) - 1

        exit = None
        while hi >= lo: 
            mid = (hi + lo) // 2
            # target found in first index of middle row
            if target == matrix[mid][0]: 
                return mid
            elif target > matrix[mid][0]: 
                lo = mid + 1
                exit = "lo"
            else: # target < matrix[mid][0]
                hi = mid - 1
                exit = "hi"
        
        if exit == "lo": 
            lo = lo - 1
        if exit == "hi" and hi >= 0: 
            lo = hi
        
        return lo

    def bin_srch(self, row: list[int], target: int) -> int: 
            """Returns the row index of matrix in which the target may be located
            Inputs: 
            - row: list of integers
            - target: integer
            Returns: 
            - in_matrix: bool indicating if target is located in row
            """
            lo = 0
            hi = len(row) - 1

            while hi >= lo: 
                mid = (hi + lo) // 2
                # target found in first index of middle row
                if target == row[mid]: 
                    return True
                elif target > row[mid]: 
                    lo = mid + 1
                else: # target < row[mid]
                    hi = mid - 1
            
            return False

    def search_matrix_two(self, matrix: list[list[int]], target: int) -> bool: 
        """Returns a bool indicating if target is in matrix
        Inputs: 
        - matrix: 2D array of integers
            integers in each row are sorted left to right
            first integer of each row is greater than the last integer of the previous row
        - target: integer
        Returns: 
        - in_matrix: bool that is true if target is in matrix, false otherwise
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        lo = 0 
        hi = num_rows * num_cols - 1

        while hi >= lo: 
            mid = (hi + lo) // 2
            mid_row = mid // num_cols
            mid_col = mid - mid_row * num_cols
            # check middle num
            if target == matrix[mid_row][mid_col]: 
                return True
            elif target > matrix[mid_row][mid_col]: 
                lo = mid + 1
            else: # target < matrix[mid_row][mid_col]:
                hi = mid - 1
        
        return False


def test(matrix: list[list[int]], target: int, ans: bool) -> None:
    Sol = Solution()
    # replace Sol.search_matrix_two w/ Sol.search_matrix to test first solution
    in_matrix = Sol.search_matrix_two(matrix, target)  
    print("Target:", target)
    print("In matrix?,", in_matrix)
    assert in_matrix == ans

def main(): 
    # test true
    mat = [ [1, 3, 5, 7], 
            [10, 11, 16, 20],
            [23, 30, 34, 60] ]
    mat_set = set()  # used for false test cases
    for i in range(len(mat)): 
        for j in range(len(mat[0])): 
            test(mat, mat[i][j], True)
            mat_set.add(mat[i][j])  # used for false test cases

    # test false
    i = 0
    while i < 50: 
        test_num = randint(-10, 100)
        while test_num in mat_set: 
            test_num = randint(-10, 100)
        test(mat, test_num, False)
        i += 1

    # edge cases
    print("test cases")
    test([[]], 4, False)
    test([[1]], 1, True)

    
    print("All Test Cases Passed!")


if __name__ == "__main__": 
    main()
        
        

        
            
            



