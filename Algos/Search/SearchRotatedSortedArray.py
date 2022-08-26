from random import randint

class Solution (object): 
    """https://leetcode.com/problems/search-in-rotated-sorted-array/"""

    def search_tf(self, nums: list[int], target: int) -> bool: 
        """Returns True if target is in nums, an array in ascending order which may be rotated
        Inputs: 
        - nums: list of integers sorted in ascending order
            *nums may be rotated at pivot k such that num = num[k:] + nums[:k]
        - target: target value in nums
        Returns: 
        - in_matrix: bool that is True if target in nums
        """
        if len(nums) == 0: 
            return False

        nums = self.unrotate_array_tf(nums)

        lo = 0
        hi = len(nums) - 1

        while hi >= lo: 
            mid = (hi + lo) // 2

            if nums[mid] == target: 
                return True
            elif target < nums[mid]: 
                hi = mid - 1
            else: # target > nums[mid]
                lo = mid + 1
        
        return False

    def unrotate_array_tf(self, nums: list[int]) -> None: 
        """Returns the array nums, which is sorted in ascending order except for a rotation, in sorted order
        Inputs: 
        - nums: list of integers sorted in ascending order
            *nums may be rotated at pivot k such that num = num[k:] + nums[:k]
        """
        lo = 0
        hi = len(nums) - 1

        if nums[lo] < nums[hi]: 
            return nums

        while hi >= lo: 
            mid = (hi + lo) // 2
            # check if mid is target
            if nums[mid] > nums[mid+1]: 
                mid = mid + 1
                break
            # check if mid + 1 is target
            elif nums[mid] < nums[mid-1]: 
                break
            elif nums[mid] < nums[lo]: 
                hi = mid - 1
            else: # nums[mid] > nums[hi]; 
                lo = mid + 1
        
        unrotated_nums = nums[mid:] + nums[:mid]
        return unrotated_nums

    def search_idx(self, nums: list[int], target: int) -> bool: 
        """Returns index of target if it is in nums, otherwise return -1. Nums is a list of integers in ascending order and can be a rotate array
        Inputs: 
        - nums: list of integers sorted in ascending order
            *nums may be rotated at pivot k such that num = num[k:] + nums[:k]
        - target: target value in nums
        Returns: 
        - target_idx: integer indicating index of target value in nums
        """
        if len(nums) == 0: 
            return -1
            
        if len(nums) == 1: 
            return -1 + (nums[0] == target)

        unrotated_nums, k = self.unrotate_array_idx(nums)
        num_spots_rotated = len(nums) - k

        lo = 0
        hi = len(unrotated_nums) - 1

        while hi >= lo: 
            mid = (hi + lo) // 2

            if unrotated_nums[mid] == target: 
                target_idx = mid - num_spots_rotated
                if target_idx < 0: 
                    target_idx = len(nums) + target_idx
                return target_idx
            elif target < unrotated_nums[mid]: 
                hi = mid - 1
            else: # target > nums[mid]
                lo = mid + 1
        
        return -1

    def unrotate_array_idx(self, nums: list[int]) -> None: 
        """Returns the array nums, which is sorted in ascending order except for a rotation, in sorted order
        Inputs: 
        - nums: list of integers sorted in ascending order
            *nums may be rotated at pivot k such that num = num[k:] + nums[:k]
        """
        lo = 0
        hi = len(nums) - 1

        if nums[lo] < nums[hi]: 
            return nums, 0

        while hi >= lo: 
            mid = (hi + lo) // 2
            # check if mid is target
            if nums[mid] > nums[mid+1]: 
                mid = mid + 1
                break
            # check if mid + 1 is target
            elif nums[mid] < nums[mid-1]: 
                break
            elif nums[mid] < nums[lo]: 
                hi = mid - 1
            else: # nums[mid] > nums[hi]; 
                lo = mid + 1
        
        unrotated_nums = nums[mid:] + nums[:mid]
        return unrotated_nums, mid
    
        
def test_tf(nums, target, ans): 
    Sol = Solution()
    in_array = Sol.search_tf(nums, target)
    assert in_array == ans

def test_idx(nums, target, ans): 
    Sol = Solution()
    target_idx = Sol.search_idx(nums, target)
    assert target_idx == ans


def main(): 

    nums = [15, 23, 32, 47, 68, -9, -4, 0, 3, 11]

    # true cases
    for num in nums: 
        test_tf(nums, num, True)

    # false cases
    nums_set = set(nums)
    i = 0
    while i < 200: 
        test_num = randint(-10, 100)
        while test_num in nums_set: 
            test_num = randint(-10, 100)
        test_tf(nums, test_num, False)
        i += 1
    
    # edge cases
    test_tf([], 4, False)
    test_tf([1, 5, 7, 13], 7, True)
    test_tf([1, 5, 8, 14], 20, False)

    nums = [4, 5, 6, 7, 10, 14, 16, -54, -2, -1, 0, 1, 3]
    # true cases
    for i in range(len(nums)): 
        test_idx(nums, nums[i], i)

    # false cases
    nums_set = set(nums)
    i = 0
    while i < 50: 
        test_num = randint(-50, 100)
        while test_num in nums_set: 
            test_num = randint(-10, 100)
        test_idx(nums, test_num, -1)
        i += 1

    # edge cases
    test_idx([], 5, -1)
    test_idx([1, 5, 7, 8], 5, 1)
    test_idx([1, 5, 7, 8], 20, -1)

    print("All Test Cases Passed!")

if __name__ == "__main__": 
    main()

            