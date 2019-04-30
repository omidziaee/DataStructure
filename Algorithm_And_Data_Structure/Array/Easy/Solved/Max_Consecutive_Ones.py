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
                    # Append the position of zeros to the list
                    dic.append(i)
                else:
                    # [] is the key point as it obliges the values be a list
                    dic = [i]
        maxOneLen = 0
        for i in range(1, len(dic)):
            # One zero is added in front of the list
            if dic[i] - dic[i - 1] - 1 > maxOneLen:
                # One reside between zeros
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
    
    def findMaxOnes(self, nums):
        tempLen = 0
        maxLen = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                tempLen += 1
                # It seems this max func takes time!!
                #maxLen = max(maxLen, tempLen)
                if tempLen > maxLen:
                    maxLen = tempLen
            else:
                tempLen = 0
        return maxLen
    # New and good
    def find_max_ones(self, nums):
        # Todo: Edge cases
        # This is acutlly a temprorry counter as soon as we arrive to zero we reset it
        one_counter = 0
        max_one_counter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                one_counter += 1
            else:
                max_one_counter = max(max_one_counter, one_counter)
                one_counter = 0
        # This is just if the last num in nums is one also
        if nums[-1] == 1:
            max_one_counter = max(max_one_counter, one_counter)
        return max_one_counter
    
    def find_max_ones_two_pointer(self, nums):
        # This is to find the first one position
        for k in range(len(nums)):
            if nums[k] == 1:
                break
        left_pointer = k
        right_pointer = k
        max_one_counter = 0
        for i in range(k, len(nums)):
            if nums[i] == 1:
                # Both of them right and left should be pointers to an index if here
                # it is put right_pointer += 1 then in max_one_conter we should not add
                # one as we already step forward the index one here
                right_pointer = i
            else:
                max_one_counter = max(max_one_counter, right_pointer - left_pointer + 1)
                left_pointer = i + 1
                right_pointer = i + 1
        # If the last num is one the else statement won't get fired. So we need another check
        # just for the case if the last num is one!!
        if nums[-1] == 1:
            max_one_counter = max(max_one_counter, right_pointer - left_pointer + 1)
        return max_one_counter
    
    def find_max_ones_one_pointer(self, nums):
        #Todo: edge cases
        for k in range(len(nums)):
            if nums[k] == 1:
                break
        left_pointer = k
        max_one_counter = 0
        for i in range(k, len(nums)):
            if nums[i] != 1:
                max_one_counter = max(max_one_counter, i - left_pointer)
        if nums[-1] == 1:
            max_one_counter = max(max_one_counter, i - left_pointer + 1)
        return max_one_counter
                   
            
    
    
sol = Solution()
print sol.maxConsecOnes([1, 1 , 0 , 1])
                            
            
