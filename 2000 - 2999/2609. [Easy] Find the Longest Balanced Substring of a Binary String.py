# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        def helper(s, bit):
            ans = []
        
            tmp = 0 
        
            for char in s: 
                if char == bit: 
                    tmp += 1 

                else: 
                    tmp = 0 

                ans.append(tmp)
                
            return ans 
                
        n = len(s)
        
        left = helper(s, "0")
        right = helper(s[:: -1], "1")[:: -1]
        
        ans = 0 
        
        for i in range(n - 1):
            ans = max(ans, min(left[i], right[i + 1]))
            
        return 2*ans 
            
