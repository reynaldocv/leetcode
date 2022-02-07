# https://leetcode.com/problems/push-dominoes/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        def helper(string):
            ans = [inf for _ in range(n)]
            process = False
            cnt = 0 
            for (i, char) in enumerate(string): 
                if char == "L":
                    process = False
                    cnt = 0 
                elif char == "R":
                    process = True 
                    cnt = 1 
                elif process: 
                    cnt += 1 
            
                if process: 
                    ans[i] = cnt
            
            return ans 
                
        n = len(dominoes)    
        
        cmp = {"L": "R", "R": "L", ".": "."}
        tmp = "".join([cmp[char] for char in dominoes])
        
        left = helper(dominoes)        
        right = helper(tmp[::-1])[::-1]
        
        ans = ""        
        for i in range(n):
            if left[i] == right[i]:
                ans += "."
            elif left[i] < right[i]:
                ans += "R"
            else:
                ans += "L"
                
        return ans
                    
        
            
                
        
        
        
        
        
        
        
        
        
        
        
        
