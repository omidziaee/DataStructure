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
        candidates.sort()
        return self.to_find_all_path(candidates, target, ans, curr_path, 0)
    def to_find_all_path(self, candidates, target, ans, curr_path, start_index):
        if target == 0:
            return ans.append(curr_path)
        for i in range(start_index, len(candidates)):
            if target - candidates[i] >= 0:
                self.to_find_all_path(candidates, target - candidates[i], ans, curr_path + [candidates[i]], i)
            else: 
                break
        return ans
    
            
            
            
sol = Solution()
print sol.combinationSum([2, 3, 6, 7], 7)