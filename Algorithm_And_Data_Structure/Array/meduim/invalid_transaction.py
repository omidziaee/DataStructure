'''
Created on Aug 26, 2019

@author: omid
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount,
 and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the
 same name and is in a different city. 
Similarly the second one is invalid too.
'''
class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        res = []
        transactions_list = []
        for transaction in transactions:
            transactions_list.append(list(transaction.split(",")))
        transactions_list.sort(key = lambda x:(x[0],int(x[1])))
        for i in range(len(transactions_list)):
            if int(transactions_list[i][2]) > 1000:
                res.append(",".join(transactions_list[i]))
            for j in range(i + 1, len(transactions_list)):
                if transactions_list[i][0] == transactions_list[j][0]:
                    if int(transactions_list[j][1]) - int(transactions_list[i][1]) <= 60 and \
                    transactions_list[j][3] != transactions_list[i][3]:
                        res.append(",".join(transactions_list[i]))
                        res.append(",".join(transactions_list[j]))
        return list(set(res))
                    
                    
            
        
                
        
        
transactions = ["alex,741,1507,barcelona","xnova,683,1149,amsterdam","bob,52,1152,beijing","bob,137,1261,beijing","bob,607,14,amsterdam","bob,307,645,barcelona","bob,220,105,beijing","xnova,914,715,beijing","alex,279,632,beijing"]
sol = Solution()
print sol.invalidTransactions(transactions)
        