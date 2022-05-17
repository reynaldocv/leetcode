# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        counter = [0 for i in range(25)]
        
        for num in candidates: 
            i = 0 
            while num > 0:
                bit = num & 1
                if bit > 0: 
                    counter[i] += 1 
                
                i += 1 
                num //= 2 
                
        return max(counter)
        
        
        
