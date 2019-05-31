'''
Created on Jan 17, 2019

@author: USOMZIA
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and 
initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # It is much better to convert it to a list as we can do the stuff in place
        s_list = list(s)
        start_of_reverse = 0
        for i in range(len(s_list) + 1):
            # We check if we either arrive at the end of the list or we arrive at 
            # the space
            if i == len(s_list) or s_list[i] == ' ':
                # Here the end of the reverse should be i - 1 as the ith element is 
                # the space
                self.reverseWordsInPlace(s_list, start_of_reverse, i - 1)
                start_of_reverse = i + 1
        return ''.join(s_list)
        
        
        
        
    def reverseWordsInPlace(self, s_list, start_of_reverse, end_of_reverse):
        while start_of_reverse < end_of_reverse:
            temp = s_list[start_of_reverse]
            s_list[start_of_reverse] = s_list[end_of_reverse]
            s_list[end_of_reverse] = temp
            start_of_reverse += 1
            end_of_reverse -= 1
        return s_list
    
sol = Solution()
print sol.reverseWords("Let's take LeetCode contest")