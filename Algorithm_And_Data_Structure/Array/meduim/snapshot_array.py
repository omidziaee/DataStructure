'''
Created on Aug 11, 2019

@author: omid
'''
class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        # this array keeps the stream of changes
        self._snap = []
        # this hashmap keeps the changes to the list
        self._dic = {}

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # import copy
        # This should be copy otherwise as the self.arr gets change the dic also gets change
        # but this approch is crazy as you create a new copy of that each time think of a vey large
        # array in this case every time you are going to copy a new one from that!
        #self.cache[self.snap_id] = copy.copy(self.arr)
        # keep the last change of the indices in the hashmap
        self._dic[index] = val
        

    def snap(self):
        """
        :rtype: int
        """
        # now when you call snap it is better to append the dic to the snap
        self._snap += [self._dic] #append is also possible
        # Now clear the change set
        self._dic = {}
        return len(self._snap) - 1
        
        

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        # We are going to find the last change of the element on the index. Lets say we want to find the last value of the index 5 at 
        # the 6th snap_id. But the last time that the number in this index has changed was at snap_id 4th. So we need to traverse
        # backward and as soon as we find an element that has the last changes of this element we need to return it.
        for i in range(snap_id, -1, -1):
            if index in self._snap[i]:
                return self._snap[i][index]
        return 0
    

            




snapshot = SnapshotArray(3)
snapshot.set(0, 4)
snapshot.set(0, 16)
snapshot.set(0, 13)
snapshot.snap()
snapshot.get(0, 0)
print snapshot.snap()