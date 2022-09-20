
#   https://leetcode.com/problems/where-will-the-ball-fall/
class Solution (object): 

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


def main(): 
    Sol = Solution()
    assert Sol.findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]) == [0,1,2,3,4,-1]
    assert Sol.findBall([[-1]]) == [-1]
    assert Sol.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]) == [1,-1,-1,-1,-1]

    print("All Test Cases Passed!")


if __name__ == "__main__": 
    main()