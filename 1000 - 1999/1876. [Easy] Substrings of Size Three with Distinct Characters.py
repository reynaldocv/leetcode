# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n - 2):
            dic = {s[i] : True}
            add = True
            for j in [i + 1, i + 2]:
                if dic.get(s[j], False) == True: 
                    add = False
                    break
                else: 
                    dic[s[j]] = True
                    
            if add: 
                ans += 1
                    
        return ans
        
