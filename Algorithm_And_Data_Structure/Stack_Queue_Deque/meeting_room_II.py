'''
Created on May 5, 2019

@author: omid
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''
class Solution(object):
    def minMeetingRooms(self, intervals):
        import collections
        from collections import _heapq
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        # As we deal with the intervals we need to sort them out based
        # on the start time
        intervals.sort(key = lambda x:x[0])
        # This is the priority queue
        free_rooms = []
        # We are filling the queue with the end interval times
        _heapq.heappush(free_rooms, intervals[0][1])
        for i in range(1, len(intervals)):
            # Check the earliest end time if the earliest end time
            # is less than the start time we should pop that interval
            if free_rooms[0] <= intervals[i][0]:
                _heapq.heappop(free_rooms)
            # Any ways you need to push the new end time to the heap
            _heapq.heappush(free_rooms, intervals[i][1])
        return len(free_rooms)
    
sol = Solution()
print sol.minMeetingRooms([[0, 30],[5, 10],[15, 20]])