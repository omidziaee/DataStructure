'''
Created on Nov 4, 2019

@author: USOMZIA
In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.

Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0
'''
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        import collections
        c = collections.Counter()
        res = 0
        # answers = [5, 5, 5, 5, 5, 5] so lets say 5 represents red so the first one says 5 means it is red and 5 others
        # are also red. The first unique number increase the total number by i(others) + 1(itself)-> you can consider 
        # zero also divisible by (i + 1). It is very important to put the increament at the end or in java c[i]++!
        for i in answers:
            if c[i] % (i + 1) == 0:
                res += i + 1
            c[i] += 1
        return res
    
sol = Solution()
print sol.numRabbits([5,5,5,5,5,5,5])