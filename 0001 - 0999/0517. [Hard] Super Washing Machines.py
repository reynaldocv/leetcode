# https://leetcode.com/problems/super-washing-machines/

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)
        
        if total % n != 0: 
            return -1
        
        avg = total // n
        
        ans = prefix = 0
        
        for (i, machine) in enumerate(machines):
            ans = max(ans, abs(prefix), machine - avg)
            prefix += machine - avg
            
        return ans
