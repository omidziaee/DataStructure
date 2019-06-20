'''
This is the answer from caikehe and all the comments below

The main idea is to iterate every number in nums.
We use the number as a target to find two other numbers which make total zero.
For those two other numbers, we move pointers, l and r, to try them.

l start from left to right
r start from right to left

First, we sort the array, so we can easily move i around and know how to adjust l and r.
If the number is the same as the number before, we have used it as target already, continue. [1]
We always start the left pointer from i+1 because the combination of 0~i has already been tried. [2]

Now we calculate the total:
If the total is less than zero, we need it to be larger, so we move the left pointer. [3]
If the total is greater than zero, we need it to be smaller, so we move the right pointer. [4]
If the total is zero, bingo! [5]
We need to move the left and right pointers to the next different numbers, so we do not get repeating result. [6]

We do not need to consider i after nums[i]>0, since sum of 3 positive will be always greater than zero. [7]
We do not need to try the last two, since there are no rooms for l and r pointers.
You can think of it as The last two have been tried by all others. [8]

For time complexity
Sorting takes O(NlogN)
Now, we need to think as if the 'nums' is really really big
We iterate through the 'nums' once, and each time we iterate the whole array again by a while loop
So it is O(NlogN+N^2)~=O(N^2)

For space complexity
We didn't use extra space except the 'res'
Since we may store the whole 'nums' in it
So it is O(N)
N is the length of 'nums'
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []
        nums.sort()
        res = []
        # the last two will be taken care of becauese l starts from i + 1 and r is always the
        # last element so when we are at the -3 element l is -2 and r is -1 so all the last three will be covered
        for i in range(len(nums) - 2):
            # check for the repeated elements
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            # Now for each i we check from i + 1 to the end to find the two other elemnets 
            # that sums up to zero
            while l < r:
                if nums[i] + nums[r] + nums[l] < 0:
                    l += 1
                elif nums[i] + nums[r] + nums[l] > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
