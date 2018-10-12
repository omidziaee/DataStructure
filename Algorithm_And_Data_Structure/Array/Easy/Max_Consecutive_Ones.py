'''
Created on Sep 27, 2018

@author: USOMZIA
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''
class Solution(object):
    def maxConsecOnes(self, nums):
        nums.insert(0,0)
        nums.append(0)
        dic = []
        for i, elem in enumerate(nums):
            if elem == 0:
                if elem in dic:
                    dic.append(i)
                else:
                    dic = [i]
        maxOneLen = 0
        for i in range(1, len(dic)):
            # One zero is added in front of the list
            if dic[i] - dic[i - 1] - 1 > maxOneLen:
                maxOneLen = dic[i] - dic[i - 1] - 1
        return maxOneLen
    
    def findLenOne(self, nums):
        firstPointer = 0
        secondPointer = 0
        maxOneLen = 0
        for i in range(len(nums) - 1):
            if nums[i] == 1:
                firstPointer = i
                for j in range(i + 1, len(nums)):
                    if nums[j] == 1:
                        secondPointer = j 
                        if secondPointer - firstPointer > maxOneLen:
                            maxOneLen = secondPointer - firstPointer
                    else:
                        firstPointer = j
                        
        return maxOneLen
                
            
    
    
sol = Solution()
print sol.findLenOne([0, 0 , 0 , 1])
                            
            
