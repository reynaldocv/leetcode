# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            if num in counter: 
                return True
            
            counter[num] += 1 
        
        return False
        
