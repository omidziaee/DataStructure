<<<<<<< HEAD
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
=======
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
>>>>>>> 3d293dbbed8c9c64166d85fba65350f789394bde
print sol.toLowerCase("Hello")