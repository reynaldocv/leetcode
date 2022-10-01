# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        last = defaultdict(lambda: -1)
        
        for num in nums2: 
            while stack and stack[-1] < num: 
                elem = stack.pop() 
                
                last[elem] = num
            
            stack.append(num)
                
        return [last[num] for num in nums1]
                
        
