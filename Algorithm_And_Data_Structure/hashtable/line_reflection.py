'''
Created on Feb 8, 2020

@author: omid
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

Example 1:

Input: [[1,1],[-1,1]]
Output: true
Example 2:

Input: [[1,1],[-1,-1]]
Output: false
Follow up:
Could you do better than O(n2) ?
we need to make sure if there is a line parallel to y that mirrors all the points
'''
class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        # set can not hashes the list so we need to cast all the points to tuples
        set_points = set(tuple(point) for point in points)
        min_x, max_x = float('inf'), -float('inf')
        for point in set_points:
            x, y = point
            min_x = min(min_x, x)
            max_x = max(max_x, x)
        # casting is very important
        mid = (min_x) + (float) (max_x - min_x) / 2
        for point in set_points:
            x, y = point
            # x - mid = mid - mirror_x
            mirror_x = 2 * mid - x
            if (mirror_x, y) not in set_points:
                return False
        return True
    
'''
Java:
class Solution {
    public boolean isReflected(int[][] points) {
        int n = points.length;
        if(points == null || n == 0){
            return true;
        }
        int min_x = Integer.MAX_VALUE;
        int max_x = Integer.MIN_VALUE;
        Set<String> pointsSet = new HashSet<String>();
        for(int[] point: points){
            String s = (double)point[0] + "a" + (double)point[1];
            pointsSet.add(s);
            min_x = Math.min(min_x, point[0]);
            max_x = Math.max(max_x, point[0]);
        }
        double mid = (double)min_x + ((double)max_x - (double)min_x) / 2;
        for(int[] point: points) {
           double mirror_x = 2 * mid - (double) point[0];
            String s = mirror_x + "a" + (double)point[1];
            if(!pointsSet.contains(s)){
                return false;
            }
        }
        return true;
    }
}

'''