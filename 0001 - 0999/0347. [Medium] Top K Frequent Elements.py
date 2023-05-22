# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(lambda: 0)

        arr = []
        
        for num in nums:
            if num not in counter: 
                arr.append(num)
                
            counter[num] += 1 
            
        arr.sort(key = lambda item: -counter[item])
        
        return arr[: k]
                
        
            
        
