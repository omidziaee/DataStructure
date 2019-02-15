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
class Solution():
    def large_group_position(self, S):
        # todo: edge case
        if len(S) < 3:
            return []
        keep_large_groups = []
        left_pointer = 0
        right_pointer = 0
        find_largest = False
        for i in range(1, len(S)):
            if S[i] == S[i - 1]:
                if not find_largest:
                    left_pointer = i - 1
                    find_largest = True
                right_pointer += 1
            else:
                if right_pointer - left_pointer >= 2:
                    keep_large_groups.append([left_pointer, right_pointer])
                find_largest = False
                left_pointer = 0
                right_pointer = 0
                
                
            
                
        return keep_large_groups
    
sol = Solution()
print sol.large_group_position("abcdddeeeeaabbbcd")
