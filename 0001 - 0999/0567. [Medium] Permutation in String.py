# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def helper(cnt1, cnt2):
            for key in cnt1: 
                if cnt1[key] != cnt2[key]:
                    return False
            
            return True 
        
        counter = defaultdict(lambda: 0)        
        cnt = defaultdict(lambda: 0)
        
        n, m = len(s1), len(s2)
        
        if m < n:
            return False 
        
        for (i, char) in enumerate(s1): 
            counter[char] += 1 
            cnt[s2[i]] += 1 
            
        for (i, char) in enumerate(s2[n:] + "+"):
            if helper(cnt, counter):
                return True
            
            cnt[char] += 1 
            cnt[s2[i]] -= 1
            if cnt[s2[i]] == 0: 
                cnt.pop(s2[i])
                
        return False
                    
                
      
        
