'''
Created on Sep 27, 2018

@author: USOMZIA
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number.
 The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''
# One native way is to traverse the nums two times, first pop the max, second pop the max and after
# all find the max of the reduced version of nums
class Solution(object):
    def findThirdMax(self, nums):
        import collections
        d = collections.defaultdict()
        # To avoid the repeated items
        nums = list(set(nums))
        if len(nums) >= 3:
            # Create a map of the elments and the index that it has happened
            for i, elem in enumerate(nums):
                if elem not in d:
                    d[elem] = i
            # Pop the first two and the last one is the third max
            for i in range(3):
                maxElem = max(nums)
                result = nums.pop(d[maxElem])
        else:
            # This is for the case that the length of the array is less than three
            result = max(nums)
        return result
    # This is easier to understand just the order is important otherwise, the max's would be the same.
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        # Do not put them as nums[0] remember [3, 2, 1]!! if you put all to nums[0] then all will be 3!!!
        max_1 = -float('inf')
        max_2 = -float('inf')
        max_3 = -float('inf')
        for elem in nums:
            if elem > max_1:
                max_3 = max_2
                max_2 = max_1
                max_1 = elem
            elif elem > max_2:
                max_3 = max_2
                max_2 = elem
            elif elem > max_3:
                max_3 = elem
        return max_3
            
        
sol = Solution()
print sol.findThirdMax([2, 2, 3, 1])
            
