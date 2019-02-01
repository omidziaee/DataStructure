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
    def sub_sets(self, nums):
        #nums.sort()
        if not nums:
            return [[]]
        first_number = nums[0]
        other_number_except_first = nums[1:]
        combinations_of_other_numbers = self.sub_sets(other_number_except_first)
        combination_first_others = [ [first_number] + x for x in combinations_of_other_numbers]
        return combinations_of_other_numbers + combination_first_others
    
 
sol = Solution()
print sol.sub_sets([1, 2, 3])    