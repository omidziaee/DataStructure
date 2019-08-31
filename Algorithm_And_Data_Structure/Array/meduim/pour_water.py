'''
Created on Aug 30, 2019

@author: USOMZIA
We are given an elevation map, heights[i] representing the height of the terrain at that index. The width at each index is 1.
 After V units of water fall at index K, how much water is at each index?

Water first drops at index K and rests on top of the highest terrain or water at that index. Then, it flows according to the following rules:

If the droplet would eventually fall by moving left, then move left.
Otherwise, if the droplet would eventually fall by moving right, then move right.
Otherwise, rise at it's current position.
Here, "eventually fall" means that the droplet will eventually be at a lower level if it moves in that direction. Also, "level" 
means the height of the terrain plus any water in that column.
We can assume there's infinitely high terrain on the two sides out of bounds of the array. Also, there could not be partial water 
being spread out evenly on more than 1 grid block - each unit of water has to be in exactly one block.

The final answer is [2,2,2,3,2,2,2]:
'''
class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        if K < 0 or K > len(heights):
            raise Exception("sth is wrong")
        while V > 0:
            # This is an initialization for the last_index if it finds any index then change this accordingly!
            last_index = -1
            # Traverse the left side
            for i in range(K - 1, -1, -1):
                # This one is very important to be here and break otherwise it tries to jump their height
                if heights[i] > heights[i + 1]:
                    break
                if heights[i + 1] > heights[i]:
                    last_index = i
            if last_index != -1:
                V -= 1
                heights[last_index] += 1
                continue
            last_index = -1
            for i in range(K + 1, len(heights)):
                # This one is very important to be here and break otherwise it tries to jump their height
                if heights[i] > heights[i - 1]:
                    break
                elif heights[i - 1] > heights[i]:
                    last_index = i
            if last_index != -1:
                V -= 1
                heights[last_index] += 1
            # Finally, if the last_index is still -1 it means neither left nor right can handle the drop
            # So we keep it at the same place
            else:
                V -= 1
                heights[K] += 1   
        return heights
    
heights = [2,1,1,2,1,2,2]
V = 4
K = 3
sol = Solution()
print sol.pourWater(heights, V, K)