'''
Created on Sep 22, 2019

@author: omid
Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:

0 < i, i + 1 < j, j + 1 < k < n - 1
Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L 
to the element indexed R.
Example:

Input: [1,2,1,2,1,2,1]
Output: True
Explanation:
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
Note:
1 <= n <= 2000.
Elements in the given array will be in range [-1,000,000, 1,000,000].
'''
class Solution(object):
    def splitArray_brute_force(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # In the brute force we need to find the bounds of i, j and k and then loop over them
        # based on the question condition 1<=i<=n - 6, i + 2 <= j <= n - 4, j + 2 <= k <= n - 2
        def calc_sum(nums, l, r): # This function calculate the sum between l and r (exclusive for r)
            ans = 0
            for i in range(l, r):
                ans += nums[i]
            return ans
        
        # Considering the constraints 
        if len(nums) < 7:
            return False
        n = len(nums)
        for i in range(1, n - 5):
            sum_i = calc_sum(nums, 0, i)
            for j in range(i + 2, n - 3):
                sum_j = calc_sum(nums, i + 1, j)
                for k in range(j + 2, n - 1):
                    sum_k = calc_sum(nums, j + 1, k)
                    sum_n = calc_sum(nums, k + 1, n)
                    if sum_i == sum_j and sum_k == sum_n and sum_j == sum_n:
                        return True
        return False
    
    def splitArray(self, nums):
        # We can create a cumulative sum to eliminate the helper and reduce the
        # time to o(n^3) and also one of the loops we can add a set to reduce to
        # o(n^2) (search in set is o(1))
        cum_sum = [0 for _ in range(len(nums))]
        cum_sum[0] = nums[0]
        for i in range(1, len(nums)):
            cum_sum[i] = cum_sum[i - 1] + nums[i]
        # from the question statement: 
        # cum_sum[len(nums)] = cum_sum[i - 1] + nums[i] + (cum_sum[j - 1] - cum_sum[i + 1]) + nums[j] + 
        # (cum_sum[k - 1] - cum_sum[j + 1]) + nums[k] + (cum_sum[k + 1] - cum_sum[len(nums) - 1])     
        # which is 4 * cum_sum[i - 1] + nums[i] + nums[j] + nums[k]
        # we first find for i and j and then if we found it for each j we create a set and keep it in the set
        for j in range(3, len(nums) - 3):
            search_set = set()
            for i in range(1, j - 1):
                if cum_sum[j - 1] - cum_sum[i] == cum_sum[i - 1]:
                    search_set.add(cum_sum[i - 1]) 
            for k in range(j + 2, len(nums) - 1):
                # With defining the set and this in we reduce one loop
                if cum_sum[len(nums) - 1] - cum_sum[k] == cum_sum[k - 1] - cum_sum[j] and cum_sum[k - 1] - cum_sum[j] in search_set:
                    return True
                
        return False
                
            
            
            
            
            
    
            
        
        
        
        
        
        
        
        
        
        
        