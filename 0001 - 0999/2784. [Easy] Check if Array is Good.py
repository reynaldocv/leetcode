# https://leetcode.com/problems/check-if-array-is-good/

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            counter[num] += 1 
            
            if num > n: 
                return False 
            
            if num < n and counter[num] > 1: 
                return False 
            
        return counter[n] == 2
