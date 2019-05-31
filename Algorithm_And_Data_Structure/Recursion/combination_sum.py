'''
Created on May 31, 2019

@author: omid
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        curr_path = []
        return self.helper(candidates, target, 0, ans, curr_path)
    def helper(self, candidates, target, curr_index, ans, curr_path):
        if target == 0:
            return ans.append(curr_path)
        if target < 0:
            return [[]]
        if curr_index >= len(candidates):
            return [[]]
        while target >= 0:
            self.helper(candidates, target, curr_index + 1, ans, curr_path + [candidates[curr_index]])
            target -= candidates[curr_index]
        return ans
            
sol = Solution()
print sol.combinationSum([2, 3, 6, 7], 7)