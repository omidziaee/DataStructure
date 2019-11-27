'''
Created on Sep 20, 2019

@author: USOMZIA
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

 

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
'''
class Solution(object):
    def minIncrementForUnique_not_working(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Edge case
        dic_counter = {}
        for elem in A:
            if elem in dic_counter:
                dic_counter[elem] += 1
            else:
                dic_counter[elem] = 1
        counter = 0
        res = []
        for elem in A:
            if dic_counter[elem] > 1:
                elem += 1
                while elem in dic_counter:
                    elem += 1
                    counter += 1
                dic_counter[elem] = 1
        for key in dic_counter:
            res.append(key)
        return counter
    def minIncrementForUnique(self, A):
        import collections
        # The idea is to count the repeated elements and find the gaps between elements to put the repeated ones in between
        dic_counter = collections.defaultdict()
        for elem in A:
            if elem in dic_counter:
                dic_counter[elem] += 1
            else:
                dic_counter[elem] = 1
        # list of repeated items
        repeated_items = []
        ans = 0
        # As the question said the maximum number in A is less than 10000
        if not A:
            return 0
        for i in range(2 * (max(A) + 1)):
            if i in dic_counter:
                if dic_counter[i] > 1:
                    repeated_items.extend([i] * (dic_counter[i] - 1))
            elif repeated_items and i not in dic_counter:
                ans += i - repeated_items.pop()
        return ans
    
    def minIncrementForUnique_second(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        counter = [0 for _ in range(2 * (max(A) + 1))]
        for elem in A:
            counter[elem] += 1
        ans, taken = 0, 0
        for i in range(len(counter)):
            if counter[i] > 1:
                taken += counter[i] - 1
                ans -= i * (counter[i] - 1)
            elif taken > 0 and counter[i] == 0:
                taken -= 1
                ans += i
        return ans
                

A = [1,1,1,1,1,1]   
sol = Solution()
print sol.minIncrementForUnique(A)