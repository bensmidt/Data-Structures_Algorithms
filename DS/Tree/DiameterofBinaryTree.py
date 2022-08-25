from src.Tree import TreeNode, BinaryTree

class Solution (object): 
    def diameter_of_binary_tree(self, root: TreeNode) -> int: 
        """Returns the longest path between any two nodes in a binary tree (diameter)
        Inputs: 
        - root: root of the binary tree
        Returns: 
        - diameter: diameter of the binary tree
        """
        height, diam = self.diam_helper(root)
        return diam

    def diam_helper(self, node: TreeNode) -> tuple: 
        """Returns the max height and longest diameter of a given tree
        Inputs: 
        - node: a node in a binary tree
        Returns: 
        - height: height if the tree in which that node is considered the root
        - diameter: diameter if that node is considered the root
        """
        # parent node is leaf node; diameter and height = 0
        if node == None: 
            return 0, 0

        else: 
            # get height and diameter of subtrees
            lc_height, l_diam = self.diam_helper(node.left)
            rc_height, r_diam = self.diam_helper(node.right)

            cur_height = max(lc_height, rc_height) + 1
            cur_diam = max(l_diam, r_diam, lc_height + rc_height)

            return cur_height, cur_diam

def test(tree_ls, ans): 
    Sol = Solution()
    tree = BinaryTree()
    tree.add_list(tree_ls)
    diam = Sol.diameter_of_binary_tree(tree.root)
    print(diam) 
    assert diam == ans

def main(): 
    test([20, 10, 30, 5, 15], 3)


if __name__ == "__main__": 
    main()

