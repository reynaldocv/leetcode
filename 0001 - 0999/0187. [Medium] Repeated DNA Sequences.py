# https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10: 
            return []
        
        key = s[:10]
        seen = {key: 1}
        maxRepeated = 1
        
        for i in range(10, n):
            key = key[1:] + s[i]
            seen[key] = seen.get(key, 0) + 1
            maxRepeated = max(seen[key], maxRepeated)
        
        if maxRepeated > 1: 
            ans = [key for key in seen if seen[key] == maxRepeated]
        else: 
            ans = []
        
        return ans
        
