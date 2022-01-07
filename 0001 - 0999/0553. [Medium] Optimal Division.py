# https://leetcode.com/problems/optimal-division/

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        strNums = [str(num) for num in nums]
        
        if len(strNums) <= 2: 
            return "/".join(strNums)
        else: 
            return strNums[0] + "/(" + "/".join(strNums[1:]) + ")"
       
                
            
            
            
