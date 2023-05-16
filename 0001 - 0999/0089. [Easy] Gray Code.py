# https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0 for _ in range(2**n)]
        
        ans[1] = 1 
        
        for i in range(1, n):
            value = 2**i
            
            start = 2**i  
            end = 2**i - 1
            
            for _ in range(2**i):
                ans[start] = value + ans[end]
                
                start += 1 
                end -= 1 
                
        return ans 
            
        
