# https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        
        n = len(nums)
        
        aSum, tmp = 0, 0
        
        for num in nums: 
            if num in seen: 
                tmp = num 
            else: 
                aSum += num
                
            seen.add(num)
            
        return (tmp, n*(n + 1)//2 - aSum)
        
