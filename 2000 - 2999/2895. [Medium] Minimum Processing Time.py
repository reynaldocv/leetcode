# https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        n = len(tasks) 
        
        tasks.sort()
        
        tmp = []
        
        for i in range(n//4):
            aux = 0
            
            for j in range(4):
                aux = max(aux, tasks[4*i + j])
                
            tmp.append(aux)
            
        tmp.sort() 
        processorTime.sort(key = lambda item: -item)
        
        ans = 0 
        
        for i in range(n//4):
            ans = max(ans, tmp[i] + processorTime[i])
            
        return ans 
            
        
        
        
