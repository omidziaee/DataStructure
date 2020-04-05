'''
Created on Mar 26, 2020

@author: omidziaee
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, 
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated
 sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than
once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
'''
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        dic_counter = {}
        res = []
        for i in range(len(s) - 9):
            if s[i: i + 10] in dic_counter:
                dic_counter[s[i: i + 10]] += 1
                if dic_counter[s[i: i + 10]] == 2:
                    res.append(s[i: i + 10])
            else:
                dic_counter[s[i: i + 10]] = 1
        return res


'''
class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        List<String> res = new ArrayList<>();
        if(s.length() < 10){
            return res;
        }
        Map<String, Integer> mapSeen = new HashMap<>();
        for(int i = 0; i < s.length() - 9; i++){
            String temp = s.substring(i, i + 10);
            mapSeen.put(temp, mapSeen.getOrDefault(temp, 0) + 1);
            if(mapSeen.get(temp) == 2){
                res.add(temp);
            }
        }
        return res;
    }
}
'''