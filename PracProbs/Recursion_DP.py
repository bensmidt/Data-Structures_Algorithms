
class RecDP (object): 
    def triple_step (self, n): 
        """Calculates possible ways to climb stairs with n steps given you can take 1, 2, or 3 steps
        Args: 
            n (int): number of steps in the stairs
            returns (int): number of possible ways to climb up the stairs
        """

        # define first four steps with 0 being zero stairs
        posbl_steps_ls = [1, 1, 2]

        # use dp to grap rest of steps
        i = 3
        while i <= n: 
            # define options if taken steps from previous steps
            one_step = i - 1
            two_step = i - 2
            three_step = i - 3

            cur_posbl_steps = posbl_steps_ls[one_step] + posbl_steps_ls[two_step] + posbl_steps_ls[three_step]
            posbl_steps_ls.append(cur_posbl_steps)
            i += 1

        return posbl_steps_ls[n]

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


    def robot_grid (self, matrix): 
        """Calculate a valid path for a robot to travel through a matrix


        """
        pass

def main(): 
    Test = RecDP()

if __name__ == "__main__": 
    main()
