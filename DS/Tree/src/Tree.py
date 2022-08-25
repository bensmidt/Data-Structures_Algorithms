
class TreeNode (object): 
    def __init__(self, val = None, left = None, right = None): 
        self.val = val 
        self.left = left
        self.right = right

class BinaryTree (object): 
    def __init__(self, root = None): 
        self.root = None

    def add_node (self, val): 
        """Adds data to a binary tree
        Input:
        - val: value of node to be added
        """

        # empty tree, set node to be root
        if self.root == None: 
            self.root = TreeNode(val)
            return
        
        cur = self.root 
        while True: 
            if val <= cur.val: 
                if cur.left == None: 
                    cur.left = TreeNode(val)
                    break
                cur = cur.left
            # greater than, go right
            else: 
                if cur.right == None: 
                    cur.right = TreeNode(val)
                    break
                cur = cur.right

        return

    def add_list(self, node_list: list, as_is = True):  
        """Adds a list of data to the binary tree
        Input: 
        - node_list: a list values to be added to binary tree
        - as_is: flag that changes adding to values based on position in list instead of order
        """
        for i in range(len(node_list)): 
            self.add_node(node_list[i])

        return


    def print(self): 
        print(self.array())

    def array(self): 
        """Returns an array representing a binary tree"""
        # empty tree
        if self.root == None: 
            return []

        cur = self.root

        tree = [[]]  # 2D-list storing tree elements
        lvl = 0  # root 
        self.arr_helper(self.root, lvl, tree)

        tree_array = []  # 1D-list representing tree elements
        for i in range(len(tree)):
            for j in range(len(tree[i])): 
                tree_array.append(tree[i][j])
        return tree_array

    def arr_helper(self, node, lvl, memo): 
        # leaf node, return
        if node == None: 
            return 

        else: 
            # try to add node value to its respective level in linked list
            try: 
                memo[lvl].append(node.val)
            # else add another level (list) to memo and add the value
            except: 
                memo.append([])
                memo[lvl].append(node.val)

            # add children nodes
            self.arr_helper(node.left, lvl+1, memo)
            self.arr_helper(node.right, lvl+1, memo)


def main():
    Tree = BinaryTree()

    node_list = [4, 2, 7, 1, 3, 6, 9]
    node_list = [4, 7, 2, 9, 6, 3, 1]
    Tree.add_list(node_list)
    Tree.print()

if __name__ == "__main__": 
    main()
