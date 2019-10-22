'''
Created on Oct 15, 2019

@author: omid
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array 
into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
'''
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        nums.sort()
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        ans = []
        curr_path = []
        visited = [False for _ in range(len(nums))]
        self.dfs(nums, ans, curr_path, total_sum / k, 0, visited)
        return ans, len(ans)
    def dfs(self, nums, ans, curr_path, target, start, visited):
        if target == 0:
            return ans.append(curr_path)
        for i in range(start, len(nums)):
            if target > 0 and not visited[i]:
                visited[i] = True
                self.dfs(nums, ans, curr_path + [nums[i]], target - nums[i], i + 1, visited)
                visited[i] = False
        return ans
    
nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
k = 5
sol = Solution()
print sol.canPartitionKSubsets(nums, k)