'''
Created on Aug 28, 2019

@author: USOMZIA
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
'''
class Solution(object):
    def maximumSwap_max_possible_number(self, num):
        """
        :type num: int
        :rtype: int
        """
        bucket = [[] for _ in range(10)]
        num_str = str(num)
        for i, num in enumerate(num_str):
            bucket[int(num)].append(i)
        ans = []
        for j in range(len(bucket) - 1, -1, -1):
            for k in range(len(bucket[j])):
                ans.append(str(j))
        return int("".join(ans))
    
    def maximumSwap(self, num):
        num_str = list(str(num))
        # This bucket keeps the index of last occurance of each digit
        bucket = [-float("inf") for _ in range(10)]
        for i, elem in enumerate(num_str):
            bucket[int(elem)] = i
        # Now we traverse the digits from left to right and check if any larger numbers occured in front it
        # then we need to swap it. Now change the max num
        for i in range(len(num_str)):
            # We need to check the bucket backward just for the numbers greater than the current number
            for j in range(9, int(num_str[i]), -1):
                # Now need to check if the index of bigger number is after the current number
                if bucket[j] > i:
                    self.swap(num_str, bucket[j], i)
                    return int("".join(num_str))
        return num
    def swap(self, lst, second, first):
        temp = lst[second]
        lst[second] = lst[first]
        lst[first] = temp
        
    def maximumSwap_brute_force(self, num):
        # There are at most 8 digits as the question said so we nee do check for C(8, 2) = 8!/6!2! = 28 cases
        # and chose the maximum
        num_str = list(str(num))
        import copy
        # It is essential to use copy otherwise whatever happens to the original list the same will be seen in the
        # other one!! a = num_str is wrong it is totally wrong!! Also it is possible to use a = num_str[:] this is 
        # the same as writting a loop and make each element equal to eachother.
        # a = num_str[:] => for i in range(len(num_str)): a[i] = num_str[i]
        a = copy.copy(num_str)
        for i in range(len(num_str)):
            for j in range(i + 1, len(num_str)):
                self.swap(num_str, j, i)
                if int("".join(a)) < int("".join(num_str)):
                    a = copy.copy(num_str)
                # Now we need to swap back to get the original number for further steps
                self.swap(num_str, i, j)
        return int("".join(a))
        

sol = Solution()
print sol.maximumSwap_brute_force(98368)










