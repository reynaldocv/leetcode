# https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/

class Solution:
    def maximumTime(self, time: str) -> str:
        hours = ["0" + str(num) for num in range(10)]
        minutes = ["0" + str(num) for num in range(10)]
        
        for num in range(10, 24):
            hours.append(str(num))
            
        for num in range(10, 60):
            minutes.append(str(num))
            
        ans = ["00", "00"]
        
        for hour in hours:         
            add = True 
            
            for i in range(2):
                if time[i] != "?" and time[i] != hour[i]:
                    add = False
                    
                    break 
                    
            if add: 
                ans[0] = max(ans[0], hour)
                
        for minute in minutes:         
            add = True 
            
            for i in range(2):
                if time[3: ][i] != "?" and time[3: ][i] != minute[i]:
                    add = False
                    
                    break 
                    
            if add: 
                ans[1] = max(ans[1], minute)
                
        return ":".join(ans)
                
                    
                        
                    
                
            
        
        
            
        
        
        
        
            
        
