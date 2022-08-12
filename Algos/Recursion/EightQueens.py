
class Solution (object): 
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

def main(num_cases = 8): 
    # eight queens answers
    ans = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200]
    for i in range(1, num_cases+1): 
        Sol = Solution(i)
        assert Sol.solve() == ans[i]
    
    print("All {} eight_queens Test Cases passed!".format(i))

if __name__ == "__main__": 
    main()