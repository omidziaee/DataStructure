'''
Created on Jan 1, 2019

@author: omid
'''
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        occurance_of_elements = {}
        for num in nums:
            if num in occurance_of_elements:
                occurance_of_elements[num] += 1
            else:
                occurance_of_elements[num] = 1
        for num, occurance in occurance_of_elements.items():
            if occurance == 2:
                result.append(num)
        return result
    
sol = Solution()
print sol.findDuplicates([4,3,2,7,8,2,3,1])
