# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        stack = [nums2[0]]
        
        for num in nums2[1:]:
            while stack and stack[-1] < num: 
                seen[stack.pop()] = num
            
            stack.append(num)
        
        for num in stack: 
            seen[num] = -1
        
        ans = []
        for num in nums1:
            ans.append(seen[num])
            
        return ans
        
