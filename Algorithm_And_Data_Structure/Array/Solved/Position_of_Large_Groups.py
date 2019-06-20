'''
Created on Sep 27, 2018

@author: USOMZIA
In a string_leet_code S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string_leet_code like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.

 

Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
 

Note:  1 <= S.length <= 1000
'''
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        find_large_group = False
        slow_pointer = 0
        fast_pointer = 0
        result = []
        for index in range(1, len(S)):
            if S[index] == S[index - 1]:
                if not find_large_group:
                    slow_pointer = index - 1
                    find_large_group = True
                fast_pointer = index 
            else:
                if fast_pointer - slow_pointer >= 2:
                    result.append([slow_pointer, fast_pointer])
                find_large_group = False
                slow_pointer = 0 
                fast_pointer = 0
        # This is just for the one if the last chars make the group!!
        # Otherwise because in this case it never goes to else for the last group
        if fast_pointer - slow_pointer >= 2:
            result.append([slow_pointer, fast_pointer])
                    
        return result
                    
S = "abbxxxxzzy"      
sol = Solution()
print sol.largeGroupPositions(S)