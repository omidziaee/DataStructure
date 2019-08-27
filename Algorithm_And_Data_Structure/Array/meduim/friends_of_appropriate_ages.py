'''
Created on Aug 26, 2019

@author: USOMZIA
Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:

Input: [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
'''
class Solution(object):
    def numFriendRequests_not_good(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        if len(ages) < 2:
            return 0
        map_age = {}
        for age in ages:
            if age in map_age:
                map_age[age] += 1
            else:
                map_age[age] = 1
        freindships = 0
        for i in range(len(ages)):
            for j in range(i + 1, len(ages)):
                if ages[i] == ages[j]:
                    freindships += 2
                elif (ages[i] > 100 and ages[j] < 100) or (ages[i] < 100 and ages[j] > 100):
                    break
                elif (ages[i] > 0.5 * ages[j] + 7 and ages[i] < ages[j]) or (ages[j] > 0.5 * ages[i] + 7 and ages[j] < ages[i]):
                    freindships += 1
        return freindships
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        # This is a bucket sort question see as the last age is limited it is the best to use the bucket_sort
        # Using Hashmap is not helpfull as you should to have sth sorted
        # It has value between 0 to 120 inclusive
        ans = 0
        count = [0 for _ in range(122)]
        # Creating the bucket
        for age in ages:
            count[age] += 1
        # We use extra space to get faster result as it is faster to run nested loop on counte than the ages
        for age_A in range(len(count)):
            # This is important as we need to compare both age_A and age_B
            for age_B in range(len(count)):
                # Now simulate whatever the question asks for. Of course we know age_B >= age_A
                if age_B <= 0.5 * age_A + 7: continue
                # This is for the equal case
                if age_B > age_A: continue
                if age_B > 100 > age_A: continue
                ans += count[age_A] * count[age_B]
                # Consider the [16, 16] case then it is 2 x 2 so we need to reduce one of them
                if age_A == age_B:
                    ans -= count[age_A]
        return ans
            
            
        
        
ages = [16, 17, 18]
sol = Solution()
print sol.numFriendRequests(ages)
                
                    
                
        
















