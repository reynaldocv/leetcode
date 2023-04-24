# https://leetcode.com/problems/distribute-money-to-maximum-children/

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children 
        
        if money < 0: 
            return -1
        
        receivers = min(money // 7, children)
        
        remain = money - receivers*7 
        
        if receivers == children and remain:  
            receivers -= 1 
            
        elif receivers + 1 == children and remain == 3: 
            receivers -= 1 
            
        return receivers

        
