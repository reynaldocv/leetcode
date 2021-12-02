# https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def findGroup(i):
            ans = group[i]
            while ans != group[ans]:
                ans = group[ans]
                
            return ans
        
        n = len(s)
        group = [i for i in range(n)] 
        
        for (a, b) in pairs: 
            ga, gb = findGroup(a), findGroup(b)
            group[ga] = group[gb] = min(ga, gb)
        
        arr = defaultdict(lambda: [])
        for (i, char) in enumerate(s): 
            arr[findGroup(i)].append(char)
        
        idx = defaultdict(lambda: 0)
        for key in arr: 
            arr[key].sort()
            idx[key] = 0
    
        ans = ""
        for i in range(n):
            gi = findGroup(i)
            ans += arr[gi][idx[gi]]
            idx[gi] += 1
                
        return ans
