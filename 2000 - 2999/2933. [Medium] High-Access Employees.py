# https://leetcode.com/problems/high-access-employees/

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        access_times.sort(key = lambda item: int(item[1][: 2])*60 + int(item[1][2: ]))
        
        times = defaultdict(lambda: [])
        
        ans = set()
        
        for (user, time) in access_times: 
            seconds = int(time[: 2])*60 + int(time[2: ])
               
            end = len(times[user])            
            start = bisect_left(times[user], seconds - 59)
            
            if end - start >= 2: 
                ans.add(user)
                
            times[user].append(seconds)
                
        return ans
            
        
