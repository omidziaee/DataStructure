'''
Created on Jan 11, 2019

@author: USOMZIA
'''
class Solution():
    def __init__(self):
        import collections
        self.memo = collections.defaultdict()
    def rob(self, nums, index):
        """
        :type nums: List[int]
        :rtype: int
        """
    
    
        

  
nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
import time
start_time = time.time()
sol = Solution()
print sol.rob(nums)
print ("total time to calculte is %s" % str((time.time() - start_time)))
