<<<<<<< HEAD
'''
Created on Jan 20, 2019

@author: omid
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 
Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
'''
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # edge case
        if len(chars) < 2:
            return chars
        first_pointer = 0
        result = []
        len_chars = len(chars)
        for index in range(1, len_chars):
            counter = 0
            if chars[index] != chars[index - 1] or index == len_chars - 1:
                if index != len_chars - 1:
                    counter = index - first_pointer
                else:
                    counter = index - first_pointer + 1
                first_pointer = index 
                #result.append(chars[index - 1])
                chars.append(chars[index - 1])
                str_counter = str(counter)
                for char in str_counter:
                    #result.append(char)
                    chars.append(char)
        for i in range(len_chars):
            chars.pop(0)
        
        return chars
    
sol = Solution()
print sol.compress(["a"])
                
                
=======
'''
Created on Jan 20, 2019

@author: omid
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 
Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
'''
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # edge case
        if len(chars) < 2:
            return chars
        first_pointer = 0
        result = []
        len_chars = len(chars)
        for index in range(1, len_chars):
            counter = 0
            if chars[index] != chars[index - 1] or index == len_chars - 1:
                if index != len_chars - 1:
                    counter = index - first_pointer
                else:
                    counter = index - first_pointer + 1
                first_pointer = index 
                #result.append(chars[index - 1])
                chars.append(chars[index - 1])
                str_counter = str(counter)
                for char in str_counter:
                    #result.append(char)
                    chars.append(char)
        for i in range(len_chars):
            chars.pop(0)
        
        return chars
    
sol = Solution()
print sol.compress(["a"])
                
                
>>>>>>> 3d293dbbed8c9c64166d85fba65350f789394bde
