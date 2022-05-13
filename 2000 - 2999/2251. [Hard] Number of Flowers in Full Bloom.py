# https://leetcode.com/problems/number-of-flowers-in-full-bloom/

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:        
        counter = defaultdict(lambda: 0)
        
        for (start, end) in flowers: 
            counter[start] += 1 
            counter[end + 1] -= 1 
            
        coord = [key for key in counter]
        coord.sort()
        
        start = None
        tmp = 0 
        arr = []
        for x in coord:             
            if start != None: 
                arr.append((start, x - 1, tmp))
            
            start = x 
            tmp += counter[x]
            
        ans = []
        for person in persons: 
            idx = bisect_left(arr, (person, inf, inf))
            idx -= 1     
            if idx == -1: 
                ans.append(0)
            elif arr[idx][0] <= person <= arr[idx][1]:
                ans.append(arr[idx][2])
            else: 
                ans.append(0)
                
        return ans 
                
            
            
                
            
           
        
        
        
