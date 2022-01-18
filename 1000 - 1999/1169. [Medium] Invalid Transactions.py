# https://leetcode.com/problems/invalid-transactions/

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ans = set()
        records = defaultdict(lambda: set())
        
        for (i, transaction) in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            if int(amount) > 1000:
                ans.add(i)
            
            for t, c, idx in records[name]:
                if c != city and abs(int(t) - int(time)) <= 60:
                    ans.add(i)
                    ans.add(idx)
                                 
            records[name].add((time, city, i))
        
        ans = [transactions[i] for i in ans]
        
        return ans
            
                
        
