# https://leetcode.com/problems/minimum-moves-to-convert-string/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls) 
        
        aSum = sum(rolls)
        
        remain = mean*(n + m) - aSum 
        
        if not(n <= remain <= n*6):         
            return []
        
        
        value = remain//n 

        k = remain % n

        ans = [value for _ in range(n)]

        for i in range(k):
            ans[i] += 1 

        return ans 
