# https://leetcode.com/problems/number-of-visible-people-in-a-queue/

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        
        ans = [0 for _ in range(n)]
        popCount = 0 
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] < heights[i]:
                stack.pop()
                popCount += 1 
            
            totalCount = popCount + 1 if stack else popCount
            ans[i] = totalCount
               
            stack.append(heights[i])
            popCount = 0
            
        return ans
        
        
