# https://leetcode.com/problems/number-of-visible-people-in-a-queue/

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        
        stack = []
        
        ans = [0 for _ in range(n)]
        
        for (ith, num) in enumerate(heights[:: - 1]):
            tmp = 0 
            
            while stack and stack[0] < num: 
                tmp += 1 
                
                stack.pop(0) 
                
            ans[n - 1 - ith] = tmp
                
            if stack: 
                ans[n - 1 - ith] += 1                
                
            stack.insert(0, num)
        
        return ans 
    

