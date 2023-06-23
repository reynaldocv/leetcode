# https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        prev = -1 
        
        arr = [i + 1 for i in range(n)]
        
        while len(arr) > 1: 
            idx = (prev + k) % n 
            
            arr.pop(idx)
            
            prev = idx - 1
            n -= 1 
            
        return arr.pop()
        
