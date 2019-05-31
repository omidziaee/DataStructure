class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # This is similat to find the top k frequent elements
        # Whenever we need to sort a hashmap, we should use bucket sort
        dic_count = {}
        res = ""
        for elem in s:
            if elem in dic_count:
                dic_count[elem] += 1
            else:
                dic_count[elem] = 1
        # at most all the chars are repeated so the last inner list is that char
        bucket = [[] for _ in range(len(s))]
        for key, value in dic_count.items():
            # List is zero indexd so all the chars in the first inner list with index
            # zero are repeated one time
            bucket[value - 1].append(key)
        # Now traverse the bucket backward as we want to show the max first
        for i in range(len(bucket) - 1, -1, -1):
            if len(bucket[i]) != 0:
                # multiply the elem and the index plus one which is the number of occurance
                for char in bucket[i]:
                    res += char * (i + 1)
        return res
sol = Solution()
print sol.frequencySort("aaaccc")