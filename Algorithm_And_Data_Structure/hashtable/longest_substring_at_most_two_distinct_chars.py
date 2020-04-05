'''
Created on Mar 29, 2020

@author: omid
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
'''
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        from collections import defaultdict
        n = len(s) 
        if n < 3:
            return n
        
        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position 
        # in the sliding window
        hashmap = defaultdict()

        max_len = 2
        
        while right < n:
            # slidewindow contains less than 3 characters
            if len(hashmap) < 3:
                hashmap[s[right]] = right
                right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == 3:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                hashmap.pop(s[del_idx])
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len



'''
java
class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        int N = s.length();
        if(N < 3) {
            return N;
        }
        int right = 0, left = 0, maxLen = 0;
        Map<Character, Integer> mapLocation = new HashMap<>();
        while(right < N){
            if(mapLocation.size() < 3){
                mapLocation.put(s.charAt(right), right++);
            }
            if(mapLocation.size() == 3){
                // .values retruns a list and for list Math.min does not work
                // Math.min works for array
                int minLeft = Collections.min(mapLocation.values());
                mapLocation.remove(s.charAt(minLeft));
                left = minLeft + 1;
            }
            // No need for right - left + 1 because we already add right++ which means
            // it is in there.
            maxLen = Math.max(maxLen, right - left);
        }
        return maxLen;
    }
}
'''