# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isGreater(a, b):     
            for i in range(n):
                if a[i] < b[i]:
                    return False
                
            return True
        
        counter = defaultdict(lambda: 0)
        for char in t: 
            counter[char] += 1
        
        index, counter3 = {}, ()
        for (i, key) in enumerate(counter):
            index[key] = i
            counter3 = counter3 + (counter[key], )
    
        n = len(counter)
        start = 0
        counter2 = (0, )*n
        ans = (inf, "")
        for (i, char) in enumerate(s): 
            if char in index: 
                idx = index[char]
                counter2 = counter2[:idx] + (counter2[idx] + 1, ) + counter2[idx + 1:]
                if isGreater(counter2, counter3):
                    while s[start] not in index or counter2[index[s[start]]] > counter3[index[s[start]]]:
                        if s[start] in index:
                            idx = index[s[start]]
                            counter2 = counter2[:idx] + (counter2[idx] - 1, ) + counter2[idx + 1:]
                        start += 1               
                    ans = min(ans, (i - start, s[start: i + 1]))
                
            
        return ans[1]
                        
