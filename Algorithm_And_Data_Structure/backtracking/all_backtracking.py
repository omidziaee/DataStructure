class Solution():
    #==================[1]Subsets======================================
    # All elements are unique
    def subsets(self, nums):
        if not nums or len(nums) == 0:
            return nums
        ans = []
        subsets = []
        self.to_find_subsets(nums, ans, subsets, 0)
        return ans
    def to_find_subsets(self, nums, ans, subsets, start_index):
        ans.append(subsets)
        for i in range(start_index, len(nums)):
            self.to_find_subsets(nums, ans, subsets + [nums[i]], i + 1)
        return ans
    #==================Subsets======================================
    
    #==================[2]Combinations no repeat======================================
    #[1, 2, 3]->[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    def permutation_no_repeat(self, nums):
        if not nums or len(nums) == 0:
            return nums
        ans = []
        combination = []
        self.to_find_combination(nums, ans, combination) # No start index as it is [1 2 3] [2 1 3] so both 1 and 2 can be start
        return ans
    def to_find_combination(self, nums, ans, combination):
        if len(combination) == len(nums):
            return ans.append(combination)
        for i in range(len(nums)):
            # Check if it not repeatd otherwise it is always gonna be [1 1 1 .... 1]
            if nums[i] in combination:
                continue
            self.to_find_combination(nums, ans, combination + [nums[i]])
        return ans
    #==================Combinations no repeat======================================
    
    #==================[3]Combination sum============================================
    #[2, 3, 7] 7->[[2, 2, 3], [7]]
    def combination_sum(self, nums, target):
        if not nums or len(nums) == 0:
            return nums
        # It is good if the nums being sorted then the branches can be pruned faster
        nums.sort()
        ans = []
        combination = []
        self.to_find_combination_sum(nums, ans, combination, target, 0) # It has start index but one elem can be used more than once!
        return ans
    def to_find_combination_sum(self, nums, ans, combination, target, start_index):
        if target == 0:
            return ans.append(combination)
        for i in range(start_index, len(nums)):
            # Check if the current elem is greater than the current target!!
            if target < nums[i]:
                break
            self.to_find_combination_sum(nums, ans, combination + [nums[i]], target - nums[i], i) #It is possible to use one elem more than once
        return ans
    #==================Combination sum============================================
    
    #==================[4]Combinations repeat========================================
    # [1, 2, 2]->[[1, 2, 2], [2, 1, 2], [2, 2, 1]]
    def combination_repeat(self, nums):
        if not nums or len(nums) == 0:
            return nums
        # Here we should use sort because we are going to compare two adjacent elements
        nums.sort()
        ans = []
        combination = []
        used = [False for _ in range(len(nums))]
        self.to_find_combination_repeated(nums, ans, combination, used)
        return ans
    def to_find_combination_repeated(self, nums, ans, combination, used):
        if len(combination) == len(nums):
            return ans.append(combination)
        for i in range(len(nums)):
            # The following checkes are very important specially the one after for
            # because we might not use the one at location i but the one at location
            # i - 1 might be the same and we already used it 
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and used[i - 1]):
                continue
            used[i] = True
            self.to_find_combination_repeated(nums, ans, combination + [nums[i]], used)
            used[i] = False
        return ans
    #==================Combinations repeat========================================
    
    #==================[5]Subsets repeated===========================================
    #[1, 2, 2]->[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    def subsets_repeat(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) == 0:
            return nums
        nums.sort()
        ans = [] 
        subsets = []
        self.to_find_subsets_repeated(nums, ans, subsets, 0)
        return ans
    def to_find_subsets_repeated(self, nums, ans, subsets, start_index):
        ans.append(subsets)
        for i in range(start_index, len(nums)):
            if (i > start_index and nums[i] == nums[i - 1]): # This checked for the repeated elements
                continue
            self.to_find_subsets_repeated(nums, ans, subsets + [nums[i]], i + 1)
        return ans
    #==================Subsets repeated===========================================
    
    #==================[6]Combination sum no repeat==================================
    # [2,5,2,1,2] target = 5->[[1, 2, 2],[5]]
    def combination_sum_no_repeat(self, nums, target):
        if len(nums) == 0 or not nums:
            return []
        nums.sort()
        ans = []
        combination = []
        self.to_find_combination_sum_no_repeat(nums, ans, combination, target, 0)
        return ans
    def to_find_combination_sum_no_repeat(self, nums, ans, combination, target, start_index):
        if target == 0:
            return ans.append(combination)
        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i - 1]:
                continue
            if target >= nums[i]:
                self.to_find_combination_sum_no_repeat(nums, ans, combination + [nums[i]], target - nums[i], i + 1)
        return ans
                
            
import time
start_time = time.time()
sol = Solution()
print sol.subsets_repeat([1,2,2])
print time.time() - start_time
            

