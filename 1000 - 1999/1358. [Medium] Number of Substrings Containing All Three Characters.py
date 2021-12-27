# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0 
        last = [-1 for _ in range(3)]
        
        for (i, char) in enumerate(s):
            last[ord(char) - ord("a")] = i
            ans += 1 + min(last)
            
        return ans

class Solution2:
    def numberOfSubstrings(self, s: str) -> int:
        index = defaultdict(lambda: [])
        for (i, char) in enumerate(s): 
            index[char].append(i)
        
        ans = 0 
        n = len(s)
        
        for (i, _) in enumerate(s): 
            minIdx = 0
            for char in "abc":
                while index[char] and index[char][0] < i:
                    index[char].pop(0)
                
                idx = index[char][0] if index[char] else n            
                minIdx = max(minIdx, idx)
            
            ans += n - minIdx
            
        return ans
        
