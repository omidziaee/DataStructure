class Solution():
    def k_diff(self, nums, k):
        unique_pairs = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    unique_pairs.add((nums[i], nums[j]))
        return len(unique_pairs)
    
    def k_diff_fast(self, nums, k):
        unique_set = ()
        nums = list(set(nums))
        counter = 0
        for i in range(len(nums)):
            if nums[i] - k in unique_set:
                counter += 1
            else:
                unique_set.add(nums[i])
                
            
    
sol = Solution()
print sol.k_diff([3, 1, 4, 1, 5], 2)
    
                
                
                
                
                            