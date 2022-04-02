# https://leetcode.com/problems/number-of-ways-to-select-buildings/

class Solution:
    def numberOfWays(self, s: str) -> int:        
        def helper(s):
            ans = []
            cnt = 0 
            for char in s: 
                cnt += 1 if char == "0" else 0 
                ans.append(cnt)
                
            return ans
        
        def collaborator(s):        
            left = helper(s)
            right = helper(s[::-1])[::-1]

            ans = 0 
        
            for i in range(1, n - 1):
                if s[i] == "1":
                    ans += left[i - 1]*right[i + 1]
                    
            return ans 
        
        n = len(s)
        
        t = "".join([str(1 - int(char)) for char in s])
        
        ans = collaborator(s) + collaborator(t)
        
        return ans 
