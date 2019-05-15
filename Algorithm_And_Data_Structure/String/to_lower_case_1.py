'''
Created on Jan 14, 2019

@author: omid
'''
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        str_list = list(str)
        for index in range(len(str_list)):
            str_list[index].lower()
        return ''.join(str_list)
    
sol = Solution()
print sol.toLowerCase("Hello")