# https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        heap = []
        
        tasks.append([inf, inf])
    
        arr = [(startTime, processingTime, idx) for (idx, (startTime, processingTime)) in enumerate(tasks)]
        
        arr.sort()
        
        last = 0 
        
        for (start, processing, idx) in arr: 
            while heap and last < start:                
                (processingTime, index, startTime) = heappop(heap)
                
                ans.append(index)
                
                last = max(last, startTime) + processingTime
                
            heappush(heap, (processing, idx, start))
            
        return ans 

            
class Solution2:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        
        arr = [(startTime, processingTime, idx) for (idx, (startTime, processingTime)) in enumerate(tasks)]
        
        arr.sort()
        
        heap = []
        
        ans = []
        
        last = 0
        
        while arr: 
            while tasks and arr[0][0] <= last:
                (_, processingTime, idx) = arr.pop(0)
                
                heappush(heap, (processingTime, idx))
            
            if not heap: 
                if arr: 
                    (startTime, processingTime, idx) = arr.pop(0)
                    
                    last = startTime + processingTime
                    
                    ans.append(idx)
            
            else: 
                (processingTime, idx) = heappop(heap)
                
                last += processingTime
                
                ans.append(idx)
                
        while heap: 
            (processingTime, idx) = heappop(heap)
            
            ans.append(idx)
            
        return ans 
            
        
                
                
                
            
        
        
        
    
