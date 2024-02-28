# https://leetcode.com/problems/array-of-doubled-pairs/

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        def helper(nums):
            counter = defaultdict(lambda: 0)
            
            for num in nums:
                counter[num] += 1 
                
            for num in nums: 
                if counter[num] > 0:
                    if counter[2*num] > 0: 
                        counter[num] -= 1 
                        counter[2*num] -= 1 
                        
                    else: 
                        return False
                    
            return True 
        
        positive = []
        negative = []
        
        for num in arr: 
            if num >= 0: 
                positive.append(num)
                
            else: 
                negative.append(num)
                
        positive.sort()
        negative.sort(key = lambda item: -item)
        
        return helper(positive) and helper(negative)
