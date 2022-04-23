# https://leetcode.com/problems/design-an-atm-machine/

class ATM:
    def __init__(self):
        self.values = [20, 50, 100, 200, 500]
        self.counter = [0, 0, 0, 0, 0]
        
    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.counter[i] += banknotesCount[i]
            
    def withdraw(self, amount: int) -> List[int]:
        tmp = amount
        idx = 4
        ans = [0 for _ in range(5)]
        aSum = 0 
        while tmp > 0 and idx >= 0:
           
            while tmp >= self.values[idx] and self.counter[idx] > 0:
                bills = min(tmp//self.values[idx], self.counter[idx])
                
                tmp -= self.values[idx]*bills
                aSum += self.values[idx]*bills
                
                self.counter[idx] -= bills
                ans[idx] += bills
                
            idx -= 1 
        
        if aSum == amount:
            return ans 
        else: 
            self.deposit(ans)
            return [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
