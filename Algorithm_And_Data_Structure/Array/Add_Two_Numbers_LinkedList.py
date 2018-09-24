'''
Created on Sep 18, 2018

@author: USOMZIA
'''
class ListNode(object):
    def __init__(self, val = None, next = None):
        self.value = val
        self.next = next
    
    def  listToLinked(self, lst):
        if len(lst) == 1:
            return ListNode(lst)
        return ListNode(lst[0], listToLinked(lst[1:]))
       
    
        
        
class Solution(object):
    def addTwoNum(self, l1, l2):
        carryOver = 0
        final = []
        lenNum1 = len(l1) - 1
        lenNum2 = len(l2) - 1
        lenNum = max(lenNum1, lenNum2)
        while lenNum >= 0:
            if lenNum1 >= 0:
                x = int(l1[lenNum1])
            else:
                x = 0
            if lenNum2 >= 0:
                y = int(l2[lenNum2])
            else:
                y = 0
            result = carryOver + x + y
            if result > 9:
                carryOver = 1
                result = result % 10
            final.insert(0,result)
            lenNum -= 1
            lenNum1 -= 1
            lenNum2 -= 1
        if carryOver == 1 and result == 0:
            final.insert(0,carryOver)
        return final
    
if __name__ == "__main__":
    l1 = '99'
    l2 = '1'
    listToLinked = ListNode()
    print listToLinked.listToLinked(l1)
        

            