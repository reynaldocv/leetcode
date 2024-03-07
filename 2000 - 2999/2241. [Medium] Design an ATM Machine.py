# https://leetcode.com/problems/design-an-atm-machine/

class ATM:

    def __init__(self):
        self.counter = [0, 0, 0, 0, 0]
        self.values = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for (i, values) in enumerate(banknotesCount): 
            self.counter[i] += values
    
    def withdraw(self, amount: int) -> List[int]:
        idx = 4
        
        tmp = [0 for _ in range(5)]
        
        while amount > 0 and idx >= 0:            
            if amount >= self.values[idx]:
                bills = amount//self.values[idx]
                
                minBills = min(bills, self.counter[idx])
                
                tmp[idx] = minBills
                
                amount -= minBills*self.values[idx]
                
            idx -= 1 
       
        if amount == 0: 
            for i in range(5):
                self.counter[i] -= tmp[i]
                
            return tmp
            
        else: 
            return [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
