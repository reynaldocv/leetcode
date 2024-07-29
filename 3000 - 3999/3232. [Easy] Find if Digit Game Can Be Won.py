# https://leetcode.com/problems/find-if-digit-game-can-be-won/

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        singleSum = 0 
        doubleSum = 0 
        
        aSum = 0 
        
        for num in nums: 
            if num <= 9: 
                singleSum += num 
            
            if 10 <= num <= 99: 
                doubleSum += num 
                
            aSum += num  
            
        return singleSum > aSum - singleSum or doubleSum > aSum - doubleSum
            
        
