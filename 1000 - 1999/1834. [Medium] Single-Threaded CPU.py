# https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        heap = []
        
        tasks.append([inf, inf])
    
        arr = [(a, b, i) for (i, (a, b)) in enumerate(tasks)]
        
        arr.sort()
        
        t = 0 
        for (enqueue, processing, idx) in arr: 
            while heap and t < enqueue: 
                (proc, i, enq) = heappop(heap)
                ans.append(i)
                t = max(t, enq) + proc
                
            heappush(heap, (processing, idx, enqueue))
            
        return ans 
