# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counter = {}
        for num in arr: 
            val = num % k
            counter[val] = counter.get(val, 0) + 1
    
        if counter.get(0, 0) % 2 != 0:
            return False
        
        for i in range(1, k//2 + 1):
            if counter.get(i, 0) != counter.get(k - i, 0):
                return False 
        
        return True
        
        
        
