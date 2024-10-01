# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counter = defaultdict(lambda: 0)        
         
        for num in arr:
            counter[num % k] += 1  
            
        if counter[0] % 2 == 1:
            return False
        
        for num in range(1, k//2 + 1):
            if counter[num] != counter[k - num]:
                return False
            
        return True
        
        
        
