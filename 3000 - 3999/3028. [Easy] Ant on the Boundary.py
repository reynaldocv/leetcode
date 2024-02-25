# https://leetcode.com/problems/ant-on-the-boundary/

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans, aSum = 0, 0
        
        for num in nums: 
            aSum += num 
            
            if aSum == 0: 
                ans += 1 
                
        return ans
                
