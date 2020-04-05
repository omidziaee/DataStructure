'''
Created on Jun 6, 2019

@author: USOMZIA
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        candidates = [i for i in range(1, 10)]
        target = n
        ans =[]
        combination = []
        self.to_find_all_combination(candidates, ans, combination, target, k, 0)
        return ans
    def to_find_all_combination(self, candidates, ans, combination, target, k, start_index):
        if target == 0 and len(combination) == k:
            ans.append(combination)
        for i in range(start_index, len(candidates)):
            if target - candidates[i] >= 0 and len(combination) < k:
                self.to_find_all_combination(candidates, ans, combination + [candidates[i]], target - candidates[i], k, i + 1)
            else:
                break
        return ans
    
sol = Solution()
print sol.combinationSum3(3, 9)