from random import randint

class Solution (object): 
    """https://leetcode.com/problems/search-in-rotated-sorted-array/"""

    def search(self, nums: list[int], target: int) -> bool: 
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

        nums = self.unrotate_array(nums)
        print("unrotated nums:", nums)

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

    def unrotate_array(self, nums: list[int]) -> None: 
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
        
def test(nums, target, ans): 
    Sol = Solution()
    in_array = Sol.search(nums, target)
    print(target)
    assert in_array == ans

def main(): 
    nums = [15, 23, 32, 47, 68, -9, -4, 0, 3, 11]

    # true cases
    for num in nums: 
        test(nums, num, True)

    # false cases
    nums_set = set(nums)
    i = 0
    while i < 200: 
        test_num = randint(-10, 100)
        while test_num in nums_set: 
            test_num = randint(-10, 100)
        test(nums, test_num, False)
        i += 1
    
    # edge cases
    test([], 4, False)
    test([1, 5, 7, 13], 7, True)
    test([1, 5, 8, 14], 20, False)

    print("All Test Cases Passed!")

if __name__ == "__main__": 
    main()

            