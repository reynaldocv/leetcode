# https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        counter1 = defaultdict(lambda: 0)
        counter2 = defaultdict(lambda: 0)
        
        for num1 in nums1: 
            for num2 in nums2:
                counter1[num1 + num2] += 1 
    
        for num3 in nums3: 
            for num4 in nums4:
                counter2[num3 + num4] += 1 
                
        ans = 0 
        
        for key in counter1: 
            if -key in counter2: 
                ans += counter1[key]*counter2[-key]
                
        return ans 
    
    
        
     
