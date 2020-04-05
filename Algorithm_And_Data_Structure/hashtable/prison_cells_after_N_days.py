'''
Created on Mar 27, 2020

@author: omidziaee
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes 
occupied. Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two 
adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell 
is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such 
changes described above.)

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
'''
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        # Ubviously there is a cycle because at most 2^8 (or we can say 2^6 first and last
        # are fixed) states.
        # we can shrunk N to N%(the length of the period).
        # Lets say N = 53 and the length of the period is 5
        # This means each 5 day it repeats which means N=0 and N=4 and N=8 ...
        # is the same, it goes all the way to 52. So, we don't need to calculate
        # all the way up 53 just one time is enough. But be careful this one time should be
        # after we find the cycle. This is because the cycle might not start at N = N and it might start 
        # at N = N - 3 so as we go we update the value of N.
        seen = {}
        while N > 0:
            key = tuple(cells)
            if key in seen:
                # This is the length of the period, days passed.
                t = seen[key] - N
                N %= t
            seen[key] = N
            # Now check if N is at least one 
            if N >= 1:
                N -= 1
                cells = self.next_day(cells)
        return cells
        
    def next_day(self, cells):
        new_cells = [0 for _ in range(8)]
        for i in range(8):
            # First cell and last cell should set to zero after the first day
            if (i > 0 and i < 7 and cells[i - 1] == cells[i + 1]):
                new_cells[i] = 1
            else:
                new_cells[i] = 0
        return new_cells