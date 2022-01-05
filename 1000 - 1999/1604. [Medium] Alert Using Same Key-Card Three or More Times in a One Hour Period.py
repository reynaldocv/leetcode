# https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def times(string):
            return 60*int(string[:2]) + int(string[3:])
        
        n = len(keyName)         
        arr = [(keyName[i], times(keyTime[i])) for i in range(n)]
        
        arr.sort()
        ans = set()
        
        for i in range(len(arr) - 2):
            if arr[i][0] not in ans: 
                if arr[i + 2][0] == arr[i][0]:
                    if arr[i + 2][1] - arr[i][1] <= 60:
                        ans.add(arr[i + 2][0])

        return sorted(ans)
                    
                    
        
        
