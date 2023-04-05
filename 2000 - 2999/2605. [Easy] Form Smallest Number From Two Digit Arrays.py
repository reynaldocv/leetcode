# https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        seen = set()
        
        ans = inf 
        
        num1 = inf 
        num2 = inf
        
        for num in nums1: 
            num1 = min(num1, num)
            
            seen.add(num)
            
        for num in nums2: 
            num2 = min(num2, num)
            
            if num in seen: 
                ans = min(ans, num)
                
        ans = min(ans, num1*10 + num2)
        ans = min(ans, num2*10 + num1)
        
        return ans 
