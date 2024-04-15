# https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def helper(time):
            return 60*int(time[: 2]) + int(time[3: ])
        
        n = len(keyTime)
        
        times = defaultdict(lambda: [])
        
        arr = [(helper(keyTime[i]), keyName[i]) for i in range(n)]        
        arr.sort() 
        
        seen = set()
        
        for (hour, user) in arr:
            if len(times[user]) > 1: 
                if hour - times[user][-2] <= 60: 
                    seen.add(user)
                    
            times[user].append(hour)
            
        ans = sorted([elem for elem in seen])
        
        return ans 
        
        
                    
                    
        
        
