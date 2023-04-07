# https://leetcode.com/problems/buddy-strings/

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        def helper(word):
            ans = (0, )*26
            
            for char in word: 
                idx = index[char]
                
                ans = ans[: idx] + (ans[idx] + 1, ) + ans[idx + 1: ]
                
            return ans 
            
        index = {chr(ord("a") + i): i for i in range(26)}
        
        m, n = len(s), len(goal)
        
        if m != n or helper(s) != helper(goal): 
            return False 
        
        counter = defaultdict(lambda: 0)
        
        maxCounter = 0 
        
        diff = 0 
        
        for i in range(n):
            counter[s[i]] += 1 
            maxCounter = max(maxCounter, counter[s[i]])
            
            if s[i] != goal[i]:
                diff += 1 
                
        if diff == 0: 
            return maxCounter >= 2
        
        return diff == 2
            
        
