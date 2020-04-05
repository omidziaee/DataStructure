'''
Created on Feb 8, 2020

@author: omid
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Solution: so dp[i] for i >=2 is number of ways to decode s[i - 2: i]
'''
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        # this should be one as for the second one we need it
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        for i in range(2, len(s) + 1):
            if 0 < int(s[i - 1: i]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
    
'''
Java:
class Solution {
    public int numDecodings(String s) {
        if(s.length() == 0){
           return 0; 
        }
        int n = s.length();
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = s.charAt(0) != '0' ? 1 : 0;
        for(int i = 2; i <= n; i++ ){
            int first = Integer.valueOf(s.substring(i - 1, i));
            int second = Integer.valueOf(s.substring(i - 2, i));
            if(0 < first && first < 10){
                dp[i] += dp[i - 1];
            }
            if(10 <= second && second <= 26){
                dp[i] += dp[i - 2];
            }
        }
        return dp[n];
    }
}
'''
