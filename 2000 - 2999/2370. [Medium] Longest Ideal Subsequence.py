# https://leetcode.com/problems/longest-ideal-subsequence/

index = {chr(ord("a") + i): i for i in range(26)}
        last = defaultdict(lambda: 0)        
        
        ans = 0 
        
        for char in s: 
            idx = index[char]            
            tmp = 0 
            
            for value in range(max(0, idx - k), min(26, idx + k + 1)):
                tmp = max(tmp, last[value % 26])
                
            last[idx] = tmp + 1            
            ans = max(ans, last[idx])
            
        return ans 
        
                
        
