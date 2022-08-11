class ArysStrs (object): 
    #1 Arrays/Matrices
    class WhereWilltheBallFall (object): 
        """https://leetcode.com/problems/where-will-the-ball-fall/"""
        def findBall(self, grid):
            """Returns a list of cols that balls will drop out of
            :type grid: List[List[int]]
            :rtype: List[int]
            """
            col_ls = []
            for i in range(len(grid[0])): 
                col_ls.append(self.findBallhelper(i, grid))
            
            return col_ls
    
        def stuck(self, row, col, grid): 
            """Returns whether a ball gets stuck at a position
            :type row: int
            :type col: int
            :type grid: List[List[int]]
            :rtype: Bool
            """
            
            pos_val = grid[row][col]
            right_wall = len(grid[0])
            
            if pos_val == -1: 
                if col == 0: 
                    return True
                if grid[row][col - 1] == 1: 
                    return True
                
            if pos_val == 1: 
                if col + 1 == right_wall: 
                    return True
                if grid[row][col + 1] == -1: 
                    return True
            
            return False
            
        def findBallhelper(self, col, grid): 
            """Returns the col a ball will drop out of
            :type col: int
            :type grid: List[List[int]]
            :rtype: List[int]
            """
            
            for row in range(len(grid)): 
                if self.stuck(row, col, grid): 
                    return -1
                col += grid[row][col]
            
            return col
    
    #2 Arrays/Matrices
    """https://leetcode.com/problems/spiral-matrix/"""
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # create list to store
        spiral_ls = []
        
        i = 0
        
        while len(matrix) != 0 and len(matrix[0]) != 0: 
          
          if i % 2 == 0: 
            nums = matrix.pop(0)
            for num in nums: 
              spiral_ls.append(num)
            
          if i % 2 == 1: 
            for j, ls in enumerate(matrix):
              ls.reverse()
              spiral_ls.append(ls.pop(0))
            matrix.reverse()
              
          i += 1
          
          
        return spiral_ls

class Test(object): 
    # 1
    def WhereWilltheBallFall(self): 
        test = ArysStrs.WhereWilltheBallFall()
        assert test.findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]) == [0,1,2,3,4,-1]
        assert test.findBall([[-1]]) == [-1]
        assert test.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]) == [1,-1,-1,-1,-1]

        print("All WhereWilltheBallFall Test Cases Passed!")

    # 2
    def spiralOrder(self): 
        test = ArysStrs()
        assert test.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
        assert test.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
        print("All spiral_order Test Cases Passed!")

def main(): 
    test = Test()
    
    # test.WhereWilltheBallFall()  # 1 
    # test.spiralOrder()  # 2 


if __name__ == "__main__": 
    main()
