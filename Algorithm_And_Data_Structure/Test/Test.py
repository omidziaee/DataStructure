class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        combination = []
        used = []
        self.to_find_all_perm(nums, ans, combination)
        return ans
    def to_find_all_perm(self, nums, ans, combination):
        if len(combination) == len(nums):
            ans.append(combination)
        for i in range(len(nums)):
            if nums[i] in combination:
                continue
            self.to_find_all_perm(nums, ans, combination + [nums[i]])
        return ans
sol = Solution()
print sol.permute([1,2,3])