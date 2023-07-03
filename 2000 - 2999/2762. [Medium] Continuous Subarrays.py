# https://leetcode.com/problems/continuous-subarrays/

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        maxHeap = []
        minHeap = []
        
        start = -1 
        
        ans = 0 
        
        for (i, num) in enumerate(nums): 
            while minHeap and minHeap[0][0] < num - 2: 
                _, idx = heappop(minHeap)
                
                start = max(start, idx)
                
            while maxHeap and maxHeap[0][0] < -(num + 2):
                _, idx = heappop(maxHeap)
                
                start = max(start, idx)
                
            heappush(minHeap, (num, i))
            heappush(maxHeap, (-num, i))
            
            ans += i - start 
            
        return ans 
