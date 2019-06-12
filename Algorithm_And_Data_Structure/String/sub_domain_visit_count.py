'''
Created on May 29, 2019

@author: USOMZIA
A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level,
 we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we 
 will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, 
followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input,
 and in any order), that explicitly counts the number of visits to each subdomain.

Example 1:
Input: 
["9001 discuss.leetcode.com"]
Output: 
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation: 
We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" will also be visited.
 So they will all be visited 9001 times.
'''
class Solution():
    def subDomainVisits(self, cpdomains):
        if len(cpdomains) == 0:
            return []
        dic_count = {}
        for elem in cpdomains:
            counter, whole_str = elem.split(' ')
            counter = int(counter)
            splitted_str = whole_str.split('.')
            str_comparison = ""
            for i in range(len(splitted_str) - 1, -1, -1):
                # The first one should not add a "." at the end
                if i == len(splitted_str) - 1:
                    str_comparison = splitted_str[i]
                else:
                    str_comparison = splitted_str[i] + "." + str_comparison
                if str_comparison in dic_count:
                    dic_count[str_comparison] += counter
                else:
                    dic_count[str_comparison] = counter
        res = []
        for key, value in dic_count.items():
            res.append(str(value) + " " + key)
        return res
                
sol = Solution()
print sol.subDomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])