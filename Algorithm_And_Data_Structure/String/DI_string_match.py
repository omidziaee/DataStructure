'''
Created on Feb 27, 2019

@author: USOMZIA
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
 

Example 1:

Input: "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: "III"
Output: [0,1,2,3]
Example 3:

Input: "DDI"
Output: [3,2,0,1]
'''
class Solution(object):
    def di_string_match_naive(self, S):
        asc_order = []
        des_order = []
        res = []
        for i in range(len(S) + 1):
            asc_order.append(i)
        for i in range(len(S), -1, -1):
            des_order.append(i)
        for char in S:
            if char == "D":
                res.append(asc_order.pop())
            if char == "I":
                res.append(des_order.pop())
        if S[-1] == "I":
            res.append(des_order.pop())
        else:
            res.append(asc_order.pop())
        return res 
    def di_string_match_deque(self, S):
        import collections
        deq_order = collections.deque()
        res = []
        for i in range(len(S) + 1):
            deq_order.append(i)
        for i in range(len(S)):
            if S[i] == "I":
                res.append(deq_order.popleft())
            else:
                res.append(deq_order.pop())
        res.append(deq_order.pop())
        return res
    
    def di_string_match_NO(self, S):
        dic_keep_location = {}
        res = [0 for _ in range(len(S) + 1)]
        for i, char in enumerate(S):
            if char in dic_keep_location:
                dic_keep_location[char].append(i)
            else:
                dic_keep_location[char] = [i]
        for key in dic_keep_location:
            if key == "D":
                for i in range(len(dic_keep_location[key])):
                    res[dic_keep_location[key][i]] = i
            else:
                for i in range(len(dic_keep_location[key]) - 1, 0, -1):
                    res[dic_keep_location[key][i]] = i
                    
        return res
    def di_string_match(self, S):
        lo = 0
        hi = len(S)
        res = []
        for i in range(len(S)):
            if S[i] == "I":
                res.append(lo)
                # Here it is increased so it is ready for the next one even for the last one
                lo += 1
            else:
                res.append(hi)
                hi -= 1
        return res + [lo]
                
            
        
                
    
sol = Solution()
S = "DDD"
print sol.di_string_match(S)