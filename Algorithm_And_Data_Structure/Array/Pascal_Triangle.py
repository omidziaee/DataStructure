'''
Created on Sep 25, 2018

@author: USOMZIA
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return 1
        else: 
            return list(str(11 ** rowIndex))
        
    # The complexity of this is O(n^2). The outer loop runs rowNum times and the inner loop runs len(innerArr). So 
    # if the outer counter is one the inner loop runs one time, if the outer loop is 10 the inner loop runs 10 times.
    # Therfore, the whole process runs 1 + 2 + ... + rowNums = roNums(rowNums + 1) /2 which is O(n^2)!
    def pascal(self, rowNum):
        pascalArr = []
        pascalArr.append([1])
        for j in range(1, rowNum + 1):
            innerArr = [None for _ in range(j+1)]
            innerArr[0], innerArr[-1] = 1, 1
            # Here instead of range(1, j) it would be much better to say range(1, len(innerArr) - 1)
            # the reason of the loop starts at one is because the first element is already equal to one 
            # and the same that it goes to len-1 is the last one is also equal to one!
            for k in range(1, len(innerArr) - 1):
                innerArr[k] = (pascalArr[j-1][k-1] + pascalArr[j-1][k])
            pascalArr.append(innerArr)
            
        return pascalArr

        
sol = Solution()
print sol.pascal(3)