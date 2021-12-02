# https://leetcode.com/problems/plates-between-candles/

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prev = {}
        left, right = [0]*n, [0]*n
        idxRight, idxLeft = [-1]*n, [-1]*n
        
        total = 0   
        lastL = -1
        for (i, val) in enumerate(s):
            total += 1 if val == "*" else 0                
            left[i] = total
            if val == "|":
                lastL = i
            idxLeft[i] = lastL 
            
        
        total = 0
        lastR = -1
        for (i, val) in enumerate(s[::-1]):
            total += 1 if val == "*" else 0 
            right[n - 1 - i] = total
            if val == "|":
                lastR = n - 1 - i
            idxRight[n - i - 1] = lastR 
            
        ans = []
        for (x, y) in queries: 
            if idxRight[x] <= idxLeft[y]:            
                ans.append(total - left[idxRight[x]] - right[idxLeft[y]])
            else: 
                ans.append(0)
            
        return ans
            
        
