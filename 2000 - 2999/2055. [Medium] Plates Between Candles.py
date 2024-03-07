# https://leetcode.com/problems/plates-between-candles/

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        
        last = n 
        
        for i in range(n - 1, -1, -1):
            if s[i] == "|":
                last = i 
                
            left[i] = last 
            
        first = -1 
        
        for i in range(n):
            if s[i] == "|":
                first = i 
                
            right[i] = first
            
        counter = []
        
        cnt = 0 
        
        for char in s: 
            if char == "*":
                cnt += 1 
                
            counter.append(cnt)
            
        ans = []
            
        for (a, b) in queries: 
            start = left[a]
            end = right[b]
            
            if end > start: 
                ans.append(counter[end] - counter[start])
                
            else: 
                ans.append(0)
                
        return ans 
        
            
        
