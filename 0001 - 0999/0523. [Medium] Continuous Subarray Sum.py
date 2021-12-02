# https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        aSum = 0
        counter0 = 0
        seen = {}
        position = -inf
        for (i, num) in enumerate(nums): 
            if num % k != 0:
                aSum = (aSum + num) % k                
                if aSum in seen: 
                    return True
                elif aSum == 0: 
                    return True
                seen[aSum] = True
                
            else:                         
                counter0 = counter0 + 1 if (position == i - 1) else 1
                position = i                
                if counter0 >= 2: 
                    return True
                    
        return False
            
                
                
                
                
        
