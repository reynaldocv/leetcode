# https://leetcode.com/problems/total-appeal-of-a-string/

class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        
        ans = 0
        index = defaultdict(lambda: [])

        for i in range(n - 1, -1, -1):
            char = s[i]
            index[char].append(i)
        
        for (i, char) in enumerate(s):
            index[char].pop()
            
            if index[char]:
                times = index[char][-1] - i
            else:
                times = n - i
            
            ans += (i + 1) * times
            
        return ans
