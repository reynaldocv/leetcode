# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums: 
            counter[num] = counter.get(num, 0) + 1
            
        arr  = [*counter]       
        arr.sort(reverse = True, key = lambda item: counter[item])
        
        return arr[:k]
    
            
        
