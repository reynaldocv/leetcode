# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        
        for row in matrix: 
            for num in row: 
                heappush(heap, num)
                
        for _ in range(k - 1):
            heappop(heap)
            
        return heappop(heap)
        
