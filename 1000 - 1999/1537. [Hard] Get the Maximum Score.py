# https://leetcode.com/problems/get-the-maximum-score/

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        
        seen = set() 
        
        stack = [0]
        
        for num in nums1: 
            seen.add(num)
            
        for num in nums2: 
            if num in seen: 
                stack.append(num)
            
        left = 0 
        right = 0 
            
        while stack and (nums1 or nums2):             
            while nums1 and nums1[-1] != stack[-1]:
                left += nums1.pop()
                
            while nums2 and nums2[-1] != stack[-1]:
                right += nums2.pop() % MOD 
                
            stack.pop() 
                
            left = right = max(left, right) % MOD 
                        
        return left
            
            
        
            
        
        
