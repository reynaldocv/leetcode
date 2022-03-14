# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

class Solution:
    def numSteps(self, s: str) -> int:
        arr = list(s)
        n = len(arr)
        
        ans = 0 
        
        for i in range(n - 1, -1, -1):
            if arr[i] == "0":
                ans += 1 
            elif i != 0 :                 
                idx = i 
                while idx >= 0 and arr[idx] == "1":
                    arr[idx] = "0"
                    idx -= 1 
                    
                if idx >= 0: 
                    arr[idx] = "1"
                    
                ans += 2 
                
        return ans 
                    
            
        
        
