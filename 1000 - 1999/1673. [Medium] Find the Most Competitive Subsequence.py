# https://leetcode.com/problems/find-the-most-competitive-subsequence/

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)        
        stack = [] 
        
        for (i, num) in enumerate(nums):             
            while stack and stack[-1] > num and len(stack) + n - i > k: 
                stack.pop()
                
            if len(stack) < k: 
                stack.append(num)
        
        return stack 
        
