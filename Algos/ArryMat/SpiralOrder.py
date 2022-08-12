
# https://leetcode.com/problems/spiral-matrix/

class Solution (object): 
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

def main(): 
    Sol = Solution()
    assert Sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert Sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
    print("All Test Cases Passed!")

if __name__ == "__main__": 
    main()