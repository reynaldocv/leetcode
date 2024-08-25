# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        
        ans = [num for num in nums]
        
        for (i, num) in enumerate(nums):
            heappush(heap, (num, i))
            
        for _ in range(k):
            (num, ith) = heappop(heap)

            heappush(heap, (multiplier*num, ith))
            
        while heap: 
            (num, ith) = heappop(heap)
            
            ans[ith] = num
            
        return ans 
