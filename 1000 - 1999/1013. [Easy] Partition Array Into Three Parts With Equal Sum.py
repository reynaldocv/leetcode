# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        aSum = sum(arr)
        
        if aSum % 3 != 0: 
            return False 
        
        left = 0 
        
        counter = 0 
        
        for num in arr: 
            left += num 
            
            if left == aSum//3:
                left = 0 
                counter += 1 
                
        return counter >= 3
                
            
