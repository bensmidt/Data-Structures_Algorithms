
# Cracking the Coding Interview

class Solution (object): 

    def triple_step_helper (self, n, memo): 
        if (n < 0): 
            return 0
        elif (n == 0): 
            return 1
        elif memo[n-1] > -1: 
            return memo[n-1]
        else: 
            memo[n-1] = self.triple_step_helper(n-1, memo) + self.triple_step_helper(n-2, memo) + self.triple_step_helper(n-3, memo)
            return memo[n-1]
    
    def triple_step_rec (self, n): 
        """Calculates possible ways to climb stairs with n steps given you can take 3 steps (using recursion)
        Args: 
            n (int): number of steps in the stairs
            returns (int): number of possible ways to climb up the stairs
        """
        posbl_steps_ls = []
        for i in range(n): 
            posbl_steps_ls.append(-1)

        return self.triple_step_helper(n, posbl_steps_ls)


def main(): 
    Sol = Solution()

    return 

if __name__ == "__main__": 
    main()