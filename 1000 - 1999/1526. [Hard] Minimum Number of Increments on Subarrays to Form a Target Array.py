# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:        
        stack = []
        ans = 0 
        for num in target + [0]: 
            go = True
            while stack and stack[-1] > num: 
                ans += stack[-1] - num if go else 0 
                go = False
                stack.pop()
                
            if not stack or (stack and stack[-1] != num):
                stack.append(num)
            
        return ans
        
        
        
        
