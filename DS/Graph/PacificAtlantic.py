
class Solution (object): 
    """https://leetcode.com/problems/pacific-atlantic-water-flow/
    To be quite frank, this implementation is poor. Utilization of sets would've been better to see if a cell can reach 
    an ocean (but I didn't know access time was O(1) ). The idea here is correct I believe, the execution though is simply 
    not what it could be. I need to keep moving though so here's my subpar solution. 
    """
    def pacific_atlantic(self, heights): 
        """Returns cells from which water can reach both the pacific and atlantic ocean
        The pacific ocean borders the top and right borders of the grid. The atlantic
        ocean borders the bottom and left borders of the grid. 
        Inputs: 
        - heights: 2D list representing a grid of cells. Each cell indicates the height of land of that cell
        Returns: 
        - reach_both: 2D list of coordinates indicating which cells can reach both oceans
        """
        height_rows = len(heights)
        height_cols = len(heights[0])
        # no island
        if height_rows == 0: 
            return []

        # trivial case, all cells touch both oceans
        if height_rows == 1 or height_cols == 1: 
            reach_both = []
            for i in range(height_rows): 
                for j in range(height_cols):
                    reach_both.append( [i, j] )
            return reach_both
        
        # create grids of zeros to representing whether a position can reach atlantic or pacific ocean
        # 1 will represent that the cell can reach the ocean
        reach_atl = []
        reach_pac = []
        for i in range(height_rows): 
            atl_row = []
            pac_row = []
            for j in range(height_cols):
                atl_row.append( [0, 0] )
                pac_row.append( [0, 0] )
            reach_atl.append(atl_row)
            reach_pac.append(pac_row)

        # create queues to do BFS for each ocean
        atl_queue = []
        pac_queue = []

        # makes border positions 1's and enqueue those positions to do BFS
        for i in range(height_rows): 
            reach_pac[i][0][0] = 1  # left border
            reach_pac[i][0][1] = 1  
            pac_queue.append( [i, 0] )
            reach_atl[i][height_cols-1][0] = 1  # right border
            reach_atl[i][height_cols-1][1] = 1 
            atl_queue.append( [i, height_cols-1] )

        for j in range(height_cols): 
            reach_pac[0][j][0] = 1  # top border
            reach_pac[0][j][1] = 1
            pac_queue.append( [0, j] )
            reach_atl[height_rows-1][j][0] = 1  # bottom border
            reach_atl[height_rows-1][j][1] = 1
            atl_queue.append( [height_rows-1, j] )

        # update all cells that can reach the pacific ocean
        while len(pac_queue) > 0: 
            pos = pac_queue.pop(0)
            self.can_reach(pos, heights, pac_queue, reach_pac)
        # update all cells that can reach atlantic ocean
        while len(atl_queue) > 0: 
            pos = atl_queue.pop(0)
            self.can_reach(pos, heights, atl_queue, reach_atl)

        # get values that reach both oceans
        reach_both = []
        for i in range(height_rows): 
            for j in range(height_cols): 
                # 2 = both, 1 = 1 ocean, 0 = neither ocean
                reach = reach_atl[i][j][0] + reach_pac[i][j][0]
                if reach == 2: 
                    reach_both.append( [i, j] )
        
        return reach_both

    def can_reach(self, pos, heights, queue, ocean): 
        """
        Inputs: 
        - pos: list of 2 integers indicating position on island
        - heights: 2D list representing a grid of heights on an island
        - queue: a list representing a queue for cells to search next
        - oceans_reached: 2D list representing a whether the cells can reach pacific and/or atlantic ocean
        Returns: 
            None
        """
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # directions to move/check
        height_rows = len(heights)
        height_cols = len(heights[0])
        max_rows = height_rows - 1
        max_cols = height_cols - 1
        for i in range(len(dir)): 
            cur_row = pos[0]
            cur_col = pos[1]
            # get adj row and col positions
            adj_row = pos[0] + dir[i][0]
            adj_col = pos[1] + dir[i][1]
            # check if position is in ocean
            if adj_row > max_rows or adj_row < 0: 
                continue
            if adj_col > max_cols or adj_col < 0: 
                continue
            # check if already visited
            if ocean[adj_row][adj_col][1] == 1: 
                continue
            # if current height less than adj height, add to queue and change value so it reaches ocean
            if heights[cur_row][cur_col] <= heights[adj_row][adj_col]: 
                queue.append( [adj_row, adj_col] )
                ocean[adj_row][adj_col][0] = 1
                ocean[adj_row][adj_col][1] = 1


        return

def test(heights, ans): 
    Sol = Solution()
    reach_both = Sol.pacific_atlantic(heights)
    print(reach_both)
    assert reach_both == ans
    print("Passed All Test Cases!")

def main(): 
    test([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]], [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])


if __name__ == "__main__": 
    main()

