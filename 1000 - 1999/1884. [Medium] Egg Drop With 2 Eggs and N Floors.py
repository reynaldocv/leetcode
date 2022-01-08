# https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/

class Solution:
    def twoEggDrop(self, n: int) -> int:
        ans = ceil((-1 + (1 + 4*2*n)**.5)//2)
        
        if ans*(ans + 1) != 2*n:
            ans += 1
        
        return ans
