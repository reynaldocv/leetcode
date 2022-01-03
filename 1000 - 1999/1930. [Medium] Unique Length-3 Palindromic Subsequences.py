# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        index = defaultdict(lambda: [])
        
        for (i, char) in enumerate(s): 
            index[char].append(i)
            
        candidates = {(a, b) for a in index for b in index}
                
        ans = 0
        for (a, b) in candidates: 
            if len(index[a]) >= 2:
                start = index[a][0]
                end = index[a][-1]
                idx = bisect_left(index[b], start + 1)
                if idx != len(index[b]):
                    if start < index[b][idx] < end:
                        ans += 1
            
        return ans        
        
                
                
            
        
        
