'''
Created on Jun 24, 2019

@author: USOMZIA
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
'''
# The idea is to run the most occured task then run other tasks up to the rest time of the repeated task
# again run the most occured task ans repeat. The ky point is each time in order to find the most occured task
# it is needed to sort the task list.
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        map_char = [0 for _ in range(26)]
        for i in range(len(tasks)):
            map_char[ord(tasks[i]) - ord('A')] += 1
        # The charachter does not important just the number of occurance is important
        map_char.sort()
        time = 0
        # sort in ascending order last one is greater than the first one
        while map_char[25] > 0:
            i = 0
            # Between each same job put other tasks up to n otherwise if you want to put the same job you need to wait n time as a cool down
            while i <= n:
                if map_char[25] == 0:
                    break
                if i < 26 and map_char[25 - i] > 0:
                    map_char[25 - i] -= 1
                time += 1
                i += 1
            map_char.sort()
        return time
    
sol = Solution()
# ["A", "A", "A", "B", "B"], 2 -> AB-AB-A
# ["A", "A", "A", "C", "B"], 2 -> ABCA--A
print sol.leastInterval(["A", "A", "A", "C", "B", "B", "B"], 2)
                