# https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while target != 1: 
            if maxDoubles:                 
                if target % 2 == 1: 
                    target -= 1 
                    ans +=1 
                else: 
                    target //= 2 
                    ans += 1 
                    maxDoubles -= 1 
            else: 
                ans += target - 1
                target = 1
                
        return ans
            

             
