class Solution():
    def remove_duplicate(self, nums):
        last_non_repeated = 0
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[last_non_repeated] = nums[i]
                last_non_repeated += 1
                
        return nums
    
sol = Solution()
print sol.remove_duplicate([1, 1, 2])