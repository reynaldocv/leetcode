# https://leetcode.com/problems/number-of-arithmetic-triplets/

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set() 
        
        ans = 0 
        
        for num in nums: 
            if num - diff in seen and num - 2*diff in seen: 
                ans += 1 
                
            seen.add(num)
            
        return ans 
        
