from src.Tree import TreeNode, BinaryTree
class Solution (object): 
    """https://leetcode.com/problems/path-sum-iii/"""

    # 1st solution: O(N^2)
    def path_sum(self, root, target_sum): 
        """Returns the number of paths in a tree where the sum of values along the path equals target_sum
        Input: 
        - root: TreeNode representing the root of a binary tree
        - target_sum: targeted sum for any given path
        Returns: 
        - num_paths = number of paths equaling target sum
        """
        if root == None: 
            return root

        num_paths = [0]
        self.path_sum_rec(root, target_sum, [], num_paths)
        return num_paths[0]

    def path_sum_rec(self, node: TreeNode, target_sum: int, prev_vals: list[int], num_paths: list[int]) -> None: 
        # node DNE
        if node == None: 
            return 
        else:
            cur_val = node.val
            prev_vals.append(cur_val)
            # find if any path sums equal target sum
            path_sum = 0
            for i in range(len(prev_vals) - 1, -1, -1): 
                path_sum += prev_vals[i]
                if path_sum == target_sum: 
                    num_paths[0] += 1

            self.path_sum_rec(node.left, target_sum, prev_vals, num_paths)
            self.path_sum_rec(node.right, target_sum, prev_vals, num_paths)
            
            prev_vals.pop()

    # better solution: O(N)
    def path_sum_hash(self, root, target_sum): 
        """Returns the number of paths in a tree where the sum of values along the path equals target_sum
        Input: 
        - root: TreeNode representing the root of a binary tree
        - target_sum: targeted sum for any given path
        Returns: 
        - num_paths = number of paths equaling target sum
        """
        if root == None: 
            return 0

        num_paths = [0]
        self.path_sum_rec_hash(root, target_sum, 0, {}, num_paths)
        return num_paths[0]

    def path_sum_rec_hash(self, node: TreeNode, target_sum: int, prev_sum: int, prev_vals: dict, num_paths: list[int]) -> None: 
        # node DNE 
        if node == None: 
            return 
        else: 
            # use prefix sum algorithms to calculate whether target sum can be met in a path ending in current node
            cur_val = node.val
            cur_sum = cur_val + prev_sum
            if cur_sum == target_sum: 
                num_paths[0] += 1
            if (cur_sum - target_sum) in prev_vals: 
                num_paths[0] += prev_vals[cur_sum-target_sum]

            # add current sum to prev_vals
            if cur_sum in prev_vals: 
                prev_vals[cur_sum] += 1
            else: 
                prev_vals[cur_sum] = 1

            self.path_sum_rec_hash(node.left, target_sum, cur_sum, prev_vals, num_paths)
            self.path_sum_rec_hash(node.right, target_sum, cur_sum, prev_vals, num_paths)
            
            
            # delete cur_sum to update dictionary for paths on return
            prev_vals[cur_sum] -= 1
            

def test(root, target_sum, ans): 
    Sol = Solution()
    num_paths = Sol.path_sum(root, target_sum)
    print(num_paths)
    assert num_paths == ans

def main(): 
    # too lazy to create good test cases for this problem just goint to use leetcode's
    pass


if __name__ == "__main__": 
    main()
                
