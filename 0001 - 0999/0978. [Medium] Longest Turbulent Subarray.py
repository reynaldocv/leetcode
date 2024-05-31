# https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:        
        prev = arr[0]
        greater = "="
        
        ans = 1 
        
        for num in arr: 
            if prev == num: 
                cnt = 1 
                
                greater = "="
                
            elif prev < num:
                if greater == ">":
                    greater = "<"
                    
                    cnt += 1 
                    
                else:         
                    greater = "<"
                    
                    cnt = 2 
                
            else: 
                if greater == "<":
                    greater = ">"
                    
                    cnt += 1 
                    
                else: 
                    greater = ">"
                    cnt = 2
                    
            prev = num     
            
            ans = max(ans, cnt)
            
        return ans 
                 
            
