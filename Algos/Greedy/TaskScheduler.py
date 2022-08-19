
class Solution (object): 
    """https://leetcode.com/problems/task-scheduler/
    
    My first solution worked but overthought the math and involved too many if and else 
    statements. This solution is the same idea as mine (from leetcode website) but more 
    concise and makes better use of memory
    """
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        unique_tasks = [0] * 26
        for task in tasks: 
            unique_tasks[ord(task) - ord('A')] += 1

        max_task_num = max(unique_tasks)
        num_max_tasks = unique_tasks.count(max_task_num)

        return max( len(tasks), (max_task_num-1) * (n+1) + num_max_tasks )

def main(): 
    Sol = Solution()
    print(Sol.leastInterval( ["A","A","A","B","B","B"], n = 2))
    print("All Test Cases Passed!")

if __name__ == "__main__": 
    main()