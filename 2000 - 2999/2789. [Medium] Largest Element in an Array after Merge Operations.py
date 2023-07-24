# https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        stack = []
        
        for num in nums[:: -1]: 
            if stack:
                if stack[-1] >= num: 
                    prev = stack.pop()
                    
                    stack.append(prev + num)
                    
                else: 
                    stack.append(num)
            else: 
                stack.append(num)
                
        return max(stack)
