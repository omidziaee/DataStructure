'''
Created on Sep 27, 2018

@author: USOMZIA
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
'''
class Solution(object):
    def can_place_flowers(self, flowerbed, n):
        # we need to find the three consecutibe 0 or if the first and second elem are zeros or if the last and the one before the last one is zero
        count = 0
        for i in range(len(flowerbed)):
            # Think about it like this;
            # You know that for the real case while we face three zeros the middle one can be a potential place 
            # So we got three flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0
            # Now for the cases of two zeros at the first two places and two zeros at the end we need to make exception
            # the second and the third conditions need to get or inside it!
            # Ok, if the first one and the second one is zero the constraint on i - 1 be zero should be excempt, add i == 0 then this one will not be considered
            # while the last one is zero and the current one is also zero first of all there is no i + 1 element! So, if i == 0 and it is the last element we
            # just need to check the last one, i, and the one before the last one i - 1
            # In this case we do not see any problem even for the one elemnt arrays! Nice and clean!
            # Be adviced the best checking appraoch in this case is to check i i-1 and i+1! not i i+1 and i+2!
            # The order of second condition is important it should be (i == 0 or flowerbed[i - 1] == 0) if it is other way around
            # we have issue since for the 0 index there is no i - 1 and it cause an error!
            if ((flowerbed[i] == 0 ) and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
                count += 1
                flowerbed[i] = 1
        return count >= n
    # The following does not work the exceptions has issue
    def can_place_flowers_easier(self, nums, k):
        if len(nums) < 3:
            return False
        # The only problem is when the first and second is zero and the last and one before last is also zero
        for index in range(1, len(nums) - 1):
            if nums[index] == 0 and nums[index - 1] == 0 and nums[index + 1] == 0:
                # Do not forget to replace the flower place with one this is essential otherwise that place 
                # will be considered as empty
                nums[index] = 1
                k -= 1
        # Now after we place all the flowers check for the edge cases
        if nums[0] == 0 and nums[1] == 0:
            k -= 1
        if nums[-1] == 0 and nums[-2] == 0:
            k -= 1
        return k == 0

    
sol = Solution()
print sol.can_place_flowers([1,0,0,0,0,1], 2)
