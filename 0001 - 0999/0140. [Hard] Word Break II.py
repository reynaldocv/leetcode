# https://leetcode.com/problems/word-break-ii/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def helper(idx, arr):
            if idx == n: 
                ans.append(" ".join(arr))
                
            else: 
                tmp = ""
                
                for i in range(idx, n):
                    tmp += s[i]
                    
                    if tmp in seen: 
                        arr.append(tmp)
                        
                        helper(i + 1, arr)
                        
                        arr.pop()
        
        ans = []
        
        seen = {word for word in wordDict}
        
        n = len(s)
        
        helper(0, [])
        
        return ans
            
        
        
        
