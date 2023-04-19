# https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        
        stack = [(-1, -1)]
        
        ans = 0 
        
        for (i, num) in enumerate(arr + [0]):
            while stack[-1][0] > num: 
                (number, middle) = stack.pop() 
                
                left = middle - stack[-1][1] 
                right = i - middle 
                
                ans = (ans + left*right*number) % MOD 
                
            stack.append((num, i))
            
        return ans 
    
    
        
