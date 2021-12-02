# https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        ans = []
        begin = 0
        end = len(S) 
        pos = 0
        while (pos < len(S)):
            if S[pos] == "I":
                ans.append(begin)
                begin += 1
            else:
                ans.append(end)
                end -= 1
            pos += 1
        ans.append(end)
        return ans
    
            
            
