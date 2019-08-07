'''
Created on Aug 1, 2019

@author: USOMZIA
Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ...
 endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:

Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
Explanation:

Initial state:
[0,0,0,0,0]

After applying operation [1,3,2]:
[0,2,2,2,0]

After applying operation [2,4,3]:
[0,2,5,5,3]

After applying operation [0,2,-2]:
[-2,0,3,5,3]
'''
class Solution(object):
    def getModifiedArray_not_working(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        nums = [0 for _ in range(length)]
        updates.sort(key = lambda x:(x[0], x[1]))
        merged = []
        merged.append(updates[0])
        for i in range(1, len(updates)):
            last_start_merged = merged[-1][0]
            last_end_merged = merged[-1][1]
            last_inc_merged = merged[-1][2]
            if updates[i][0] < last_end_merged:
                merged.pop()
                merged.append([last_start_merged, updates[i][0], last_inc_merged])
                merged.append([updates[i][0], last_end_merged, last_inc_merged + updates[i][2]])
                merged.append([last_end_merged, updates[i][1], updates[i][2]])
            else:
                merged.append(updates[i])
        for j in range(len(merged)):
            start = merged[j][0]
            end = merged[j][1]
            for i in range(start, end + 1):
                nums[i] += merged[i][2]
        return nums
    def getModifiedArray(self, length, updates):
        nums = [0 for _ in range(length)]
        for update in updates:
            start, end, inc = update
            nums[start] += inc
            if end < length - 1:
                nums[end + 1] -= inc
        # Now create the cumulative sum
        for i in range(1, length):
            nums[i] += nums[i - 1]
        return nums
            
            
sol = Solution()
print sol.getModifiedArray(5, [[1,3,2],[2,4,3],[0,2,-2]])
        