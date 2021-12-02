# https://leetcode.com/problems/smallest-integer-divisible-by-k/

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        res = 0 
        for i in range(k):
            res = (res*10 + 1) % k
            if res == 0: 
                return i + 1
        return -1
        
class Solution2:
    def smallestRepunitDivByK(self, k: int) -> int:
        ans = len(str(k))
    
        div = int("1"*ans)
        visited = {}
        while div not in visited and div != 0: 
            visited[div] = True        
            quo = div//k
            div -= quo*k
            if div == 0: 
                break
            div = 10*div + 1
            ans += 1
        
        return -1 if div != 0 else ans
            
        
        
