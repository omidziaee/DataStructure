'''
Created on Sep 23, 2019

@author: USOMZIA
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must 
have the same probability of being returned.
'''
class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # As hashtable is not index based we have problem when we get random. For
        # getting random we need a random generator to generate a random number
        # for random index. So for sure we need an array to keep values as well.
        self.keep_vals = []
        self.keep_vals_index = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        # So when we insert we need to append to array as well and we need to keep                                                
        # the indices as well in the hashmap, as we replace the last element of the 
        # array with the one that we are goint to pop.
        if val not in self.keep_vals_index:
            self.keep_vals.append(val)
            # Be careful about putting -1 as it is zero based index
            self.keep_vals_index[val] = len(self.keep_vals) - 1
            return True
        else:
            return False
            

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        # So for remove, first check if the hashmap already contians the value if yes 
        # get the index from hashmap and replace the last element of the array with that.
        if val in self.keep_vals_index:
            # pop(val, ->[default value]) here means if val is not there return 0
            index = self.keep_vals_index[val]
            last = self.keep_vals[-1]
            # upsate the hashmap as the index of last is going to change
            self.keep_vals_index[last] = index
            # update the array as the last will replace the one located at index
            self.keep_vals[index] = last
            # Now pop the values from hashmap and the array
            self.keep_vals_index.pop(val, 0)
            self.keep_vals.pop()
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return self.keep_vals[random.randint(0, len(self.keep_vals) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()