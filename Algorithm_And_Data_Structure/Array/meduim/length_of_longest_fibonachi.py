'''
Created on Sep 19, 2019

@author: USOMZIA
A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence, 
find the length of the longest fibonacci-like subsequence of A.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any 
number of elements (including none) from A, without changing the order of the remaining elements.  
For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)
'''
class Solution():
    def lenLongestFibSubseq_not_working(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        len_A = len(A)
        res = set()
        for i in range(len_A - 2):
            for j in range(i + 1, len_A - 1):
                for k in range(j + 1, len_A):
                    if A[i] + A[j] == A[k]:
                        res.add(A[i])
                        res.add(A[j])
                        res.add(A[k])
        return res
    def lenLongestFibSubseq_not_working_second(self, A):
        if len(A) < 3:
            return 0
        A.sort()
        res = []
        for i in range(len(A) - 2):
            l = i + 1
            r = len(A) - 1
            while l < r:
                sum_num = A[i] + A[l]
                if sum_num < A[r]:
                    while r < l and A[l] == A[l + 1]:
                        r -= 1
                    r -= 1
                elif sum_num > A[r]:
                    return res
                else:
                    res += [A[i], A[l], A[r]]
                    while l < r and A[l] == A[l + 1]:
                        l += 1
                    while l < r and A[r] == A[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        res1 = set(res)
        return res1
    
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        set_A = set(A)
        max_len = 0
        curr_len = 0
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                # x should be A[j] which is the second number not A[i]
                x, y = A[j], A[i] + A[j]
                curr_len = 2
                # So now we have two of them now lets check if the sum exists 
                # in the set.
                while y in set_A:
                    curr_len += 1
                    # Now swap x and y to create new fibbonaci number
                    # The purpose of the swap is lets say we have [1,2,3,4,5,6,7,8]
                    # so first we get 1, x = 2 then y = 1 + 2 = 3 so 3 is there 
                    # swap x = 3 and y = 2 + 3 = 5 
                    temp = x
                    x = y
                    y = temp + y
                    # x, y = y, x + y
                max_len = max(curr_len, max_len)
        return max_len if max_len > 2 else 0
                    
                           
        
        
    
A = [1,2,3,4,5,6,7,8]
sol = Solution()
print sol.lenLongestFibSubseq(A)