# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" and s == "":
            return ""
        
        counter = defaultdict(lambda: 0)
        
        for char in t: 
            counter[char] += 1 
            
        total = len(counter)
        qnt = 0
        
        cnt = defaultdict(lambda: 0)
        start = 0 
        
        ans = (inf, 0, 0)
        
        for (i, char) in enumerate(s):
            if char in counter: 
                cnt[char] += 1 
                
                if cnt[char] == counter[char]:
                    qnt += 1 
                
            while qnt == total: 
                ans = min(ans, (i - start, start, i))
                
                oldChar = s[start]
                
                if oldChar in cnt: 
                    cnt[oldChar] -= 1 
            
                    if cnt[oldChar] < counter[oldChar]:
                        qnt -= 1 
                
                start += 1
            
        return "" if ans[0] == inf else s[ans[1]: ans[2] + 1]
            
            
                
                
                
            
                
            
                        
