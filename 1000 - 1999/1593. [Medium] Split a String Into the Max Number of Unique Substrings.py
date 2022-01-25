# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def helper(idx, seen):
            nonlocal ans
            if idx == n:                
                ans = max(ans, len(seen))
            else:
                for i in range(idx + 1, n + 1):
                    subS = s[idx: i]
                    if subS not in seen:
                        seen[subS] = True
                        helper(i, seen)
                        seen.pop(subS)
                
        seen = {}
        n = len(s)
        ans = 0
        
        helper(0, seen)
        
        return ans
        
