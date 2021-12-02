# https://leetcode.com/problems/max-chunks-to-make-sorted/

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        aux = -1
        ans = 0 
        for (i, val) in enumerate(arr):
            aux = max(val, aux)
            if aux == i: 
                ans += 1
                
        return ans
        
