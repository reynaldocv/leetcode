# https://leetcode.com/problems/constrained-subsequence-sum/

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums) 
        
        heap = [(-nums[0], 0, 1)]
        
        ans = (nums[0], 1)
        
        for i in range(1, n):
            while i - heap[0][1] > k: 
                heappop(heap)
                
            cur = max((nums[i], 1), (-heap[0][0] + nums[i], heap[0][2] + 1))
            ans = max(ans, cur)
            
            heappush(heap, (-cur[0], i, cur[1]))
            
        return -1 if ans[1] == 0 else ans[0]
