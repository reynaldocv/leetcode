# https://leetcode.com/problems/maximal-score-after-applying-k-operations/

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        
        for num in nums:
            heappush(heap, -num)
            
        ans = 0
        
        for _ in range(k):
            if heap:
                elem = -heappop(heap)
                
                ans += elem 
                
                newElem = ceil(elem/3)
                
                if newElem > 0:
                    heappush(heap, -newElem)
                    
            else:
                break
                
        return ans 
