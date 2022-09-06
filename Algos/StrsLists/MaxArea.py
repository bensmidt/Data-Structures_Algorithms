
class Solution (object):

    def max_area(self, height): 
        """
        :type height: List[int]
        :rtype: int
        """
        # no two lines to connect
        if len(height) <= 1: 
            return 0
        
        start = 0 
        end = len(height) - 1
        max_area = 0
        cur_area = 0
        
        while end > start: 
            cur_area = self.area(start, end, height)
            max_area = max(max_area, cur_area)
            
            if height[start] >= height[end]: 
                end -= 1
            else: # height[end] >= height[start]: 
                start += 1
                
        return max_area
            
    def area(self, start, end, height): 
        length = min(height[start], height[end])
        width = end - start
        return width * length
            
def test(height, ans): 
    Sol = Solution()
    max_area = Sol.max_area(height)
    assert max_area == ans

def main(): 
    test([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)
    test([1, 1], 1)

    print("All Test Cases Passed!")

if __name__ == "__main__": 
    main()
