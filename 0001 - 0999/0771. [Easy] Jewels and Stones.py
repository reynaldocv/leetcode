# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = {}
        ans = 0
        for i in J: 
            jewels[i] = 1
        for i in S: 
            ans += jewels.get(i, 0)
        return ans
            
        
