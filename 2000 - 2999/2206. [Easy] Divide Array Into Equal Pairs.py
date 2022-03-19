# https://leetcode.com/problems/divide-array-into-equal-pairs/

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            counter[num] += 1 
            
        for key in counter: 
            if counter[key] % 2 == 1: 
                return False 
            
        return True
