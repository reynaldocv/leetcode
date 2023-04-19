# https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        stack = []
        
        ans = [-1 for _ in range(2*n)]
        
        for (i, num) in enumerate(nums + nums + [-inf]):
            while stack and stack[-1][0] < num: 
                (_, idx) = stack.pop()
                
                ans[idx] = num 
                
            stack.append((num, i))
                
        return ans[: n]
                
        
        
              
             
