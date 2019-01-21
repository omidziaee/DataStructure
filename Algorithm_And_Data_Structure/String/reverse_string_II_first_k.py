'''
Created on Jan 18, 2019

@author: USOMZIA
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
'''
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Chunk the string in 2*k windows and reverse the first k elements. If the length of the window is less than
        # k we reversed the whole window
        chunk_start = 0
        s_list = list(s)
        # This loop is naive because if we dont put the break it loops over the whole length of the string which is 
        # useless and time consuming!!!
        for i in range(len(s_list)):
            # This is the end of the chunk! lets say if i is zero the end would be 2 but as we need to send the index
            # be careful to send chunk_end - 1 to the reverse funciton
            chunk_end = 2*k * (i + 1)
            if chunk_end <= len(s_list):
                self.reverse_stirng(s_list, chunk_start, chunk_end - 1, k)
            else:
                # If chunk is at the end of the string, send the last index instead of chunk_end
                self.reverse_stirng(s_list, chunk_start, len(s_list) - 1, k)
                # For sure if the chucnk_end is larger than the length of the window there is no need to continue; break
                break
            # Remember to update the chunk_start
            chunk_start = chunk_end
        return ''.join(s_list)
    
    # Whenever it is a two pointer problem one of the pointers which most of the time is the second or the faster one
    # can be expressed by the loop counter 
    # The follwoing does not work because of the edge cases like if the length is one char!!!
    def reverseStr_easier_to_understand(self, s, k):
        s_list = list(s)
        for i in range(0, len(s_list), 2 * k):
            self.reverse_stirng(s_list, i, 2*k * (i + 1) - 1, k)
        return ''.join(s_list)
        
            
        
    def reverse_stirng(self, string_to_reverse, reverse_start, reverse_end, k):
        if k > reverse_end - reverse_start + 1:
            reverse_end = reverse_end
        else:
            reverse_end = reverse_start + k - 1
        while reverse_start < reverse_end:
            temp = string_to_reverse[reverse_start]
            string_to_reverse[reverse_start] = string_to_reverse[reverse_end]
            string_to_reverse[reverse_end] = temp
            reverse_end -= 1
            reverse_start += 1
        
        return string_to_reverse
        
    
sol = Solution()
print sol.reverseStr_easier_to_understand("abcdefg", 2)
    