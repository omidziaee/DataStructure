'''
Created on Sep 27, 2018

@author: USOMZIA
Given an array of integers where 1 a[i] n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''
class Solution(object):
    def dispressNum(self, nums):
        nums.sort()
        result = [] 
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                nums.insert(i + 1, nums[i] + 1)
                result.append(nums[i] + 1)
        return result
    
    def disapearedNums(self, nums):
        result = []
        # In order to make the search o(1) we need to create a set however 
        # it adds o(n) space which is not acceptable
        nums_set = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                result.append(i)
        return result
    def disapearedNums_accepted(self, nums):
        # The idea is consider each num in nums as a pointer to an index of an array element
        # for example if the num is 4 we can consider it as a pointer to index 3 (4-1 as index starts
        # from zero). So if any num from 1 to n does not exist, there is no pointer to point to that
        # index. 
        # As the question requires no extra space and o(n) we are not allowed to add a set or map.
        # The only way is to change the main array in place and then another walk another time through
        # the array and find the missed elements.
        # Ok! We can walk through the array and for each num make the array element at index num - 1 to negative
        # Its value! But first be careful in the loop you need to make the abs why? Consider [4,3,2,7,8,2,3,1]
        # as a test case. When you are checking 3 at index 1 the algorithm forces the first 2 to -2. Then the next
        # step num is -2! you can not assign it to any index! The only way is to use abs(). The algorithm is as follows:
        result = []
        # This is the first pass to negate each element that the associated index exits
        for num in nums:
            # This abs is for reverting back the sign as it is not possible to have negative indices
            num = abs(num)
            # Now check the value at that index
            if nums[num - 1] > 0:
                nums[num - 1] *= -1
        # Like in the example [4,3,2,7,8,2,3,1] there is no 5 to make 8 negative or there is 6 to make 2 at
        # index 5 (6 - 1) negative; therefore, after the first pass nums would change to [-4, -3, -2, -7, 8, 2, -3, -1]
        # Next pass is to check the positive values   
        for index, num in enumerate(nums):
            if num > 0:
                # We need to store the index of the still positive num but as the index start from zero 
                # we need to add it by one
                result.append(index + 1)
        return result
        
                
            
            
               
            
            

sol = Solution()
print sol.disapearedNums_accepted([4,3,2,7,8,2,3,1])                
                
            
