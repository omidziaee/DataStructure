'''
Created on Aug 5, 2019

@author: USOMZIA
'''
class Solution():
    def find_k_sum(self, nums, k, target):
        if len(nums) == 0:
            return []
        nums.sort()
        ans = []
        curr_path = []
        # We need both start and end inicies
        #self.helper_old(nums, ans, curr_path, target, k)
        self.helper(nums, ans, curr_path, target, k, 0)
        return ans
    def helper_old(self, nums, ans, curr_path, target, k):
        if k < 2 or k > len(nums):
            return None
        if k == 2:
            l = 0
            r = len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    ans.append(curr_path + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                    while r > 0 and nums[r] == nums[r - 1]:
                        r -= 1
                elif target > s:
                    l += 1
                else:
                    r -= 1
        for i in range(len(nums)):
            if i == 0 or i > 0 and nums[i] != nums[i - 1]:
                self.helper_old(nums[i + 1:], ans, curr_path + [nums[i]], target - nums[i], k - 1)
        return ans
    
    def helper(self, nums, ans, curr_path, target, k, start_index):
        if k < 2 or k > len(nums) - start_index:
            return None
        if k == 2:
            l = start_index
            r = len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    ans.append(curr_path + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                    while r > 0 and nums[r] == nums[r - 1]:
                        r -= 1
                elif target > s:
                    l += 1
                else:
                    r -= 1
        for i in range(start_index, len(nums) - k + 1):
            if i == start_index or i > start_index and nums[i] == nums[i - 1]:
                self.helper(nums, ans, curr_path + [nums[i]], target - nums[i], k - 1, i + 1)
            #if i > start_index and nums[i] == nums[i - 1]:
            #    continue 
            #self.helper(nums, ans, curr_path + [nums[i]], target - nums[i], k - 1, i + 1)
        return ans
    
nums = [1,0,-1,0,-2,2]
#nums = [-1, -2, -7, -3, 0]
#nums = [0, 0, 0, 0]
target = 0
sol = Solution()
print sol.find_k_sum(nums, 4, target)
                    
                    
        
            
        