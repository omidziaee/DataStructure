'''
Created on Jan 20, 2019

@author: omid
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''
class Solution():
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # This is DFS that can be done either with recursion or stack
        current_string = ''
        num = 0
        stack_keep = []
        # Traverse over the input string
        for char in s:
            # If we reach "[" it means new combination of letters
            if char == "[":
                stack_keep.append(current_string)
                stack_keep.append(num)
                # Ok after we pushed the number and the combination restart both number and current_string
                current_string = ''
                num = 0
            # If we reach "]" it means we need to update the current_string with the string pushed in the stack
            elif char == "]":
                num = stack_keep.pop()
                # The one that pops from the stack is previous_string
                previous_string = stack_keep.pop()
                # Now update the current_string with previous string and the char that is stored in the current_string
                current_string = previous_string + num * current_string
                # After you create the current_string you need to restart the num again
                num = 0
            elif char.isdigit():
                num = num * 10 + int(char) # 22 is equal to 2*10+2 and 222 is equal to 22*10+2
            
            else:
                current_string += char # [abc] we need to concatinate the chars till it is ended
        
        return current_string  
    
sol = Solution()
print sol.decodeString("2[a]3[b]") 
        