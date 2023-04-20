# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heap = []
        
        for num in nums: 
            heappush(heap, num)
            
        for _ in range(k):
            num = heappop(heap)
            
            if num == 0: 
                break 
            
            heappush(heap, -num)
            
        ans = 0 
        
        while heap: 
            ans += heappop(heap)
            
        return ans 
        
