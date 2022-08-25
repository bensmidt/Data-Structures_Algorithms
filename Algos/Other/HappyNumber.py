
class Solution (object): 
    """https://leetcode.com/problems/happy-number/"""

    def is_happy(self, n): 
        """Returns whether the sum of the digits in a number eventually converges to one or not
        Input: 
        - n : integer
        Returns: 
        - is_happy: bool indicating True if the number is happy
        """
        prev_vals = set()
        prev_vals.add(n)

        while True: 
            n = self.happy_cycle(n)
            if n in prev_vals: 
                break
            prev_vals.add(n)

        if n == 1: 
            return True

        return False

    def happy_cycle(self, n):
        """Returns the next number in a happy cycle
        Input: 
        - n: integer
        Returns: 
        - sum: integer being the output of one happy cycle
        """
        digits = []
        num = n

        while num != 0: 
            digits.append(num%10)
            num = num // 10

        sum = 0
        for digit in digits: 
            sum += digit ** 2
        
        return sum

def test(n, ans): 
    Sol = Solution()
    is_happy = Sol.is_happy(n)
    print(is_happy)
    assert is_happy == ans

def main(): 
    test(1, True)
    test(2, False)
    test(19, True)
    print("All Test Cases Passed!")

if __name__ == "__main__": 
    main()