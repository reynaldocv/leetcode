# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort() 
        
        prev = -inf 
        tmp = -1 
        
        ans = 0 
        
        for num in nums: 
            if prev != num: 
                tmp += 1 
                
            ans += tmp            
            prev = num
            
        return ans 
            
        
        
