# https://leetcode.com/problems/sum-game/

class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        sumLeft, sumRight = 0, 0
        left, right = 0, 0 
        
        for char in num[: n//2]:
            if char == "?":
                left += 1 
            else: 
                sumLeft += int(char)
        
        for char in num[n//2:]:
            if char == "?":
                right += 1 
            else: 
                sumRight += int(char)
                
        if left == right and sumLeft == sumRight: 
            return False
        
        if (left + right) % 2 == 0:
            if ((left - right)//2)*9 == sumRight - sumLeft:
                return False

        return True
