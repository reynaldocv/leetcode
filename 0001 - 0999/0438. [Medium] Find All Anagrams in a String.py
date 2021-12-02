# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def compare(counting, preCounting):
            for key in counter: 
                if counting[idx[key]] - preCounting[idx[key]] != counter[key]:
                    return False
            return True
            
        counter = defaultdict(lambda: 0)
        for char in p: 
            counter[char] += 1
            
        n = len(counter)
        
        idx = {}
        counting = ()
        for (i, key) in enumerate(counter): 
            idx[key] = i
            counting += (0, )
        
        arrCounting = [counting]
        ans = []
        for i in range(len(s)): 
            if s[i] in counter: 
                pos = idx[s[i]]
                counting = counting[: pos] + (counting[pos] + 1,) + counting[pos + 1:]
                if i >= len(p) - 1:                    
                    preCounting = arrCounting[i - len(p) + 1]
                    if compare(counting, preCounting):
                        ans.append(i - len(p) + 1)            
            arrCounting.append(counting)
        
        return ans
                
            
            
