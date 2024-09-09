# https://leetcode.com/problems/reach-end-of-array-with-max-score/

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        stack = [(0, -1)]
        
        for (ith, num) in enumerate(nums):
            if num > stack[-1][0]:
                stack.append((num, ith))
                
        n = len(nums) 
        
        last = n - 1
        
        ans = 0 
        
        while stack: 
            (num, start) = stack.pop() 
            
            ans += num*(last - start)
            
            last = start 
            
        return ans 
            
