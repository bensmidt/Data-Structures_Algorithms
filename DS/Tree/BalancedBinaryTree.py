
from src.Tree import BinaryTree, TreeNode

class Solution(object):
    def isBalanced(self, root: TreeNode) -> bool:
        """Determines if the subtrees of all nodes in a tree are balanced (differ by <= 1 in height)
        Inputs: 
        - root: TreeNode representing the root of a binary tree
        Returns
        - is_balanced: bool representing whether the tree is balanced or not
        """
        if root == None: 
          return True
        
        tree_depth, is_balanced = self.isBalanced_rec(True, root, 0)
        return is_balanced
        
    def isBalanced_rec(self, is_balanced: bool, node: TreeNode, prev_depth: int) -> tuple: 
      """Helper function for isBalanced
      Inputs: 
      - is_balanced: bool representing whether the current node contains balanced subtrees
      - node: a TreeNode in the tree
      - prev_depth: depth (height) of a node's parent node
      Returns: 
      - is_balanced: bool representing whether the current node contains balanced subtrees
      - tree_depth: depth (height) of the tree 
      """
      
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

        tree_depth = max(l_depth, r_depth)
        return tree_depth, is_balanced

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
        