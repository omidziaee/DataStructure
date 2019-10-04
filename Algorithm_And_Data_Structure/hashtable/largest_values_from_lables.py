'''
Created on Sep 30, 2019

@author: USOMZIA
We have a set of items: the i-th item has value values[i] and label labels[i].
Then, we choose a subset S of these items, such that:
|S| <= num_wanted
For every label L, the number of items in S with label L is <= use_limit.
Return the largest possible sum of the subset S.
Example: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
In this example, subset size <= 3 (as num_wanted = 3)
Listing members in each label
Label 1 -> [5,4]
Label 2 -> [3,2]
Label 3 -> [1]
Now from each label we can use only 1 element because use_limit for each label is 1.
The question asks us to find the largest possible sum of the subset, so we take from 
each label group, the largest element available.
So in this example,
from label 1 : we take 5,
from label 2: we take 3
from label 3: we take 1 (since label 1 has only one element)
5+3+1=9
'''
class Solution():
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        # The idea is to create a map for lables and as we move along update this
        # map. Then from this map we can check not to use more than use limit out of
        # lable.
        import collections
        # when you define if like this you don't need to worry about key error 
        # or if you put the array as input to counter it creates the counter with key as values 
        # in the array
        lable_counter = collections.defaultdict(int)
        val_lable_list = zip(values, labels)
        val_lable_list.sort(key = lambda x:-x[0])
        ans = []
        counter = 0
        for elem in val_lable_list:
            val, lable = elem
            if lable_counter[lable] < use_limit:
                if counter < num_wanted:
                    # remeber if it is not defined through the collections you need to check if it is zero 
                    # then make it one otherwise plus one it here but with collection no need
                    lable_counter[lable] += 1
                    counter += 1
                    ans.append(val)
        return sum(ans)
    
    def largestValsFromLabels_not_default_dic(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        # The idea is to create a map for lables and as we move along update this
        # map. Then from this map we can check not to use more than use limit out of
        # lable.
        # when you define if like this you don't need to worry about key error 
        # or if you put the array as input to counter it creates the counter with key as values 
        # in the array
        lable_counter = {}
        val_lable_list = zip(values, labels)
        val_lable_list.sort(key = lambda x:-x[0])
        ans = []
        counter = 0
        for elem in val_lable_list:
            val, lable = elem
            if counter < num_wanted:
                if lable in lable_counter:
                    if lable_counter[lable] < use_limit:
                        # remeber if it is not defined through the collections you need to check if it is zero 
                        # then make it one otherwise plus one it here but with collection no need
                        lable_counter[lable] += 1
                        counter += 1
                        ans.append(val)
                else:
                    lable_counter[lable] = 1
                    counter += 1
                    ans.append(val)
        return sum(ans)
                
        
values = [5,4,3,2,1]
labels = [1,1,2,2,3]
sol = Solution()
print sol.largestValsFromLabels(values, labels, 3, 1) 
print sol.largestValsFromLabels_not_default_dic(values, labels, 3, 1)       

        
        
        
        