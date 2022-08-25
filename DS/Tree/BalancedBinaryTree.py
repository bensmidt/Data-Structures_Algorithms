
from src.Tree import BinaryTree

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: 
          return True
        
        tree_depth, is_balanced = self.isBalanced_rec(True, root, 0)
        return is_balanced
        
    def isBalanced_rec(self, is_balanced, node, prev_depth): 
      # is leaf node
      if node == None: 
        return prev_depth, is_balanced
      
      else:         
        cur_depth = prev_depth + 1
        
        # get depth of both subtrees and whether they're balanced or not
        l_depth, l_balanced = self.isBalanced_rec(is_balanced, node.left, cur_depth)
        r_depth, r_balanced = self.isBalanced_rec(is_balanced, node.right, cur_depth)
        is_balanced = is_balanced and l_balanced and r_balanced
        
        # determine if current subtrees are balanced
        if abs(l_depth - r_depth) > 1: 
          is_balanced = False
          
        return max(l_depth, r_depth), is_balanced

def test(tree_ls, ans): 
    Sol = Solution()
    tree = BinaryTree()
    tree.add_list(tree_ls)
    is_balanced = Sol.isBalanced(tree.root)
    assert is_balanced == ans

def main(): 
    test([6, 3, 20, 15, 21], ans=True)
    test([6, 7, 20, 15, 21], ans=False)
    test([10, 11, 8, 9, 6, 7, 5], ans=False)
    
    print("All Test Cases Passed!")

if __name__ == "__main__": 
    main()
        