
class Solution(object):
    """https://leetcode.com/problems/rotting-oranges/"""

    def oranges_rotting(self, grid: list) -> int: 
        """
        Returns the number of minutes it takes for a grid of oranges to rot. If impossible to rot all oranges, returns -1
        
        Every minute any fresh orange that is 4-directionally adjacent to a rotten orange become rotten
        Input: 
        - grid: 2D list representing what's at each position in the list
            0 = empty cell
            1 = fresh orange
            2 = rotten orange
        Returns: 
        - time: integer representing the number of minutes to rot all the oranges
        """
        gray_orngs = []  # list of rotten oranges that may corrupt the next batch of fresh oranges
        fresh_orngs = 0 # number of fresh oranges
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                # add fresh oranges to a dictionary
                if grid[i][j] == 1: 
                    fresh_orngs += 1
                # add initial rotten oranges to a list (which will function as a queue)
                elif grid[i][j] == 2: 
                    gray_orngs.append( (i, j) )
        
        # all cells empty, no time elapses
        if len(gray_orngs) == 0 and fresh_orngs == 0: 
            return 0
        
        time = 0  # minutes
        while len(gray_orngs) > 0:
            num_orngs_to_visit = len(gray_orngs)
            visit_next = []
            
            for i in range(num_orngs_to_visit): 
                orng = gray_orngs.pop() # orng is a 1D list representing a position
                # visit and return next batch of fresh oranges
                rottened_orngs, fresh_orngs = self.find_fresh_orngs(orng, grid, fresh_orngs)
                # add newly rotten oranges to visit from next round
                for i in range(len(rottened_orngs)): 
                  visit_next.append( rottened_orngs[i] )
            
            gray_orngs = visit_next
            time += 1
        
        # there are no more oranges to visit, subtract the additional minute added at end
        time -= 1
        
        # not all oranges visited
        if fresh_orngs > 0: 
            time = -1

        return time 

    def find_fresh_orngs(self, pos: list , grid: list , fresh_orngs: int) -> tuple: 
        """Returns a list of lists representing the position of fresh oranges that were made rotten and will be used to visit from next minute
        Inputs: 
        - pos: position of orange to be visiting from
        - grid: 2D list representing what's at each position in the list
        - fresh_orngs: int representing the number of fresh oranges left
        Returns: 
        - visit_next: list of newly rotten oranges
        - fresh_orngs: int representing the number of fresh oranges les
        """
        visit_next = []

        # check 4 adjacent positions for fresh oranges
        for i in range(4): 
            # down
            if i == 0: 
                row = pos[0] + 1
                col = pos[1]
                # check for out of range idx
                if row >= len(grid): 
                    continue
            # up
            elif i == 1: 
                row = pos[0] - 1
                col = pos[1]
                # check for out of range idx
                if row < 0: 
                    continue
            # right
            elif i == 2: 
                row = pos[0]
                col = pos[1] + 1
                # check for out of range idx
                if col >= len(grid[0]): 
                    continue
            # left
            else: 
                new_row = pos[0]
                col = pos[1] - 1
                # check for out of range idx
                if col < 0: 
                    continue
            
            # empty cell
            if grid[row][col] == 0: 
                continue
            # fresh orange
            if grid[row][col] == 1: 
                visit_next.append( (row, col) )
                # rot the orange
                grid[row][col] = 2
                # delete from fresh_orngs dictionary
                fresh_orngs -= 1
            # rotten orange
            if grid[row][col] == 2: 
                continue
                
        return visit_next, fresh_orngs

def test(grid, ans): 
    Sol = Solution()
    assert Sol.oranges_rotting(grid) == ans

def main(): 
    test([[2,1,1],[1,1,0],[0,1,1]], ans=4)
    test([[2,1,1],[0,1,1],[1,0,1]], ans=-1)
    test([[0,2]], ans=0)

    print("All Test Cases Passed!")

if __name__ == "__main__": 
    main()

