'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution(object):
    def sub_sets_old(self, nums):
        #nums.sort()
        if not nums:
            return [[]]
        first_number = nums[0]
        other_number_except_first = nums[1:]
        combinations_of_other_numbers = self.sub_sets(other_number_except_first)
        combination_first_others = [ [first_number] + x for x in combinations_of_other_numbers]
        return combinations_of_other_numbers + combination_first_others
    def sub_sets(self, nums):
        if len(nums) == 0:
            return []
        ans = []
        sub = []
        self.to_find_all_subsets(nums, ans, sub, 0)
        return ans
    def to_find_all_subsets(self, nums, ans, sub, start_index):
        ans.append(sub)
        # it does not have stop criteria
        for i in range(start_index, len(nums)):
            self.to_find_all_subsets(nums, ans, sub + [nums[i]], i + 1) # we can not use one num more than once
        return ans
            
             
    
 
sol = Solution()
print sol.sub_sets([1, 3, 2])    