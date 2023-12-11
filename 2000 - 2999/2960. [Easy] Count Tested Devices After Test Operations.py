# https://leetcode.com/problems/count-tested-devices-after-test-operations/

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0 
        
        tmp = 0 
        
        for num in batteryPercentages: 
            if num - tmp > 0: 
                ans += 1 
                
                tmp += 1 
                
        return ans 
        
        
        
