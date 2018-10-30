'''
Created on Oct 29, 2018

@author: USOMZIA
'''
class Solution(object):
    def reverse_word(self, message):
        start_of_reverse = 0
        end_of_reverse = len(message) - 1
        
        # Call the helper function (reverse in place does not need to return anything!)
        self.reverse_arr(message, start_of_reverse, end_of_reverse)
        start_of_reverse = 0
        
        for i in range(len(message) + 1):
            # Send each word to the helper function to reverse it again
            # If we arrive at space or the end of the message we need to call the reverse function
            # It is important to figure out when to send the word to the helper function
            # Order of this (message[i] == ' ') or (i == len(message)) is important
            # As the loop goes over all consider +1 in for! As we want to move up to the end of the string!
            if (i == len(message)) or (message[i] == ' ') :
                # i is the index of space
                self.reverse_arr(message, start_of_reverse, i - 1)
                # i is the start of the space
                start_of_reverse = i + 1
            
        return message
            
                
                
                
    def reverse_arr(self, message, start_of_reverse, end_of_reverse):
        while start_of_reverse < end_of_reverse:
            temp = message[start_of_reverse]
            message[start_of_reverse] = message[end_of_reverse]
            message[end_of_reverse] = temp
            start_of_reverse += 1
            end_of_reverse -= 1
            
        return message
    

sol = Solution()
print sol.reverse_word([ 't', 'h', 'e', ' ', 'e', 'a', 'g', 'l', 'e', ' ',
  'h', 'a', 's', ' ', 'l', 'a', 'n', 'd', 'e', 'd' ])            
        
        