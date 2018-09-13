'''
Created on Aug 14, 2018

@author: USOMZIA
'''
# This program publishes a combinations of letters based on the clicked 
# phone keys.
def letterCombination(digits):
    # Create a dictionary between the numbers and letters
    d = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno","7":"pqrs", "8":"tuv", "9":"wxyz"}
    # Corner case
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return list(d[digits])
    head = digits[0]
    rest = digits[1:]
    # Now recurstion
    restCombo = letterCombination(rest)
    headCombo = d[head]
     
    # Now create a list comprehension to merge all the strings together
    return [h + s for s in restCombo for h in headCombo]
 
print letterCombination("234")
