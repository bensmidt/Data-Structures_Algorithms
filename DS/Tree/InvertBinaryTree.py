from src.Tree import TreeNode, BinaryTree

class Solution (object): 
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None: 
          return root
        
        self.invertTree_helper(root)
        
        return root
        
    def invertTree_helper(self, node): 
        # leaf node, nothing to switch
        if node == None: 
            return 
        
        else: 
            # switch subtrees
            l_subtree = node.left
            node.left = node.right
            node.right = l_subtree
            
            # invert left subtree
            self.invertTree_helper(node.left)
            
            # invert right subtree
            self.invertTree_helper(node.right)

def test(tree_ls, ans): 
    Sol = Solution()
    tree = BinaryTree()
    tree.add_list(tree_ls)
    Sol.invertTree(tree.root)
    assert tree.array() == ans

def main(): 

    tree = [4, 2, 7, 1, 3, 6, 9]
    inv_tree = [4, 7, 2, 9, 6, 3, 1]
    test(tree, inv_tree)

    tree = [2, 1, 3]
    inv_tree = [2, 3, 1]
    test(tree, inv_tree)

    print("All Test Cases Passed!")

if __name__ == "__main__": 
    main()