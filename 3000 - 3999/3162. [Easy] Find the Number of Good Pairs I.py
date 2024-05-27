# https://leetcode.com/problems/find-the-number-of-good-pairs-i/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0 
        
        for numA in nums1: 
            for numB in nums2: 
                if numA % (numB*k) == 0: 
                    ans += 1 
                    
        return ans 
            
