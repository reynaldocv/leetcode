# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        
        for num in nums: 
            heappush(heap, num)
            
        ans = 0 
        
        while len(heap) > 1 and heap[0] < k:
            num1 = heappop(heap)
            num2 = heappop(heap)
            
            heappush(heap, 2*num1 + num2)
            
            ans += 1 
            
        return ans 
        
