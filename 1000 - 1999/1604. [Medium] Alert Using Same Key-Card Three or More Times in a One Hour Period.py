# https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def times(string):
            return 60*int(string[:2]) + int(string[3:])
        
        n = len(keyName) 
        cardPass = defaultdict(lambda: [])
        
        for i in range(n):
            cardPass[keyName[i]].append(times(keyTime[i]))
            
        ans = []
        
        for key in cardPass: 
            arr = sorted(cardPass[key])
            for i in range(len(arr) - 2):
                if arr[i + 2] - arr[i] <= 60: 
                    ans.append(key)
                    break
        
        return sorted(ans)
                    
        
        
