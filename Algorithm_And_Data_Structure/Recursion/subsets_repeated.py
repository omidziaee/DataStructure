'''
Created on Jun 4, 2019

@author: omid
[1, 2, 2]->[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
'''
class Solution():
    def subsets_repeated(self, nums):
        if len(nums) == 0 or not nums:
            return []
        # Whenever there is repeated we need to sort it!
        nums.sort()
        ans = []
        subsets = []
        self.to_find_all_subsets_repeated(nums, ans, subsets, 0)
        return ans
    def to_find_all_subsets_repeated(self, nums, ans, subsets, start_index):
        ans.append(subsets)
        for i in range(start_index, len(nums)):
            #The following is to check the repeated items
            if i > start_index and nums[i] == nums[i - 1]:
                continue
            self.to_find_all_subsets_repeated(nums, ans, subsets + [nums[i]], i + 1)
        return ans
    
sol = Solution()
print sol.subsets_repeated([1, 2, 2])