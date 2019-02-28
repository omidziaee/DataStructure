class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic_keep_sum_location = {}
        # key is the sum and value is the place that sum happend
        dic_keep_sum_location[0] = [-1]
        sum_so_far = 0
        for i in range(len(nums)):
            sum_so_far += nums[i]
            if sum_so_far in dic_keep_sum_location:
                dic_keep_sum_location[sum_so_far].append(i)
            else:
                dic_keep_sum_location[sum_so_far] = [i]
        counter = 0
        if k == 0:
            counter = len(dic_keep_sum_location[0]) - 1
        else:
            for sum in dic_keep_sum_location:
                if sum - k in dic_keep_sum_location:
                    counter += len(dic_keep_sum_location[sum - k])
        
                
        return counter
                
        
sol = Solution()
print sol.subarraySum([-1, -1, 1], 0)