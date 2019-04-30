'''
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
    Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
         3
        / \
       4   5
      / \   \ 
     5   4   7

'''
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