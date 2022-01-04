# https://leetcode.com/problems/maximum-average-pass-ratio/

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        heap = []
        for (a, b) in classes: 
            heappush(heap, (a/b - (a + 1)/(b + 1), a, b))
            
        for _ in range(extraStudents):
            (_, a, b) = heappop(heap)
            a, b = a + 1, b + 1
            heappush(heap, (a/b - (a + 1)/(b + 1), a, b))
            
        ans = sum(a/b for (_, a, b) in heap)
        
        return ans/n
