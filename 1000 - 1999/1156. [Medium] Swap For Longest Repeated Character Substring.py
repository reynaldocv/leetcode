# https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        def helper(string):
            ans = []
            prev = "$"
            cnt = 0 
            for char in string: 
                if char == prev: 
                    cnt += 1 
                else: 
                    cnt = 1
                    prev = char
                ans.append((cnt, char))
                
            return ans
            
        n = len(text)
        left = helper(text)
        right = helper(text[::-1])[::-1]
        ans = 1
        
        counter = defaultdict(lambda: 0)
        for char in text: 
            counter[char] += 1 
        
        for (i, char) in enumerate(text):
            (cntL, charL) = (0, "$") if i == 0 else left[i - 1]
            (cntR, charR) = (0, "$") if i == n - 1 else right[i +  1]
            if charL == charR: 
                ans = max(ans, min(cntL + cntR + 1, counter[charL]))
            else: 
                ans = max(ans, min(cntL + 1, counter[charL]))
                ans = max(ans, min(cntR + 1, counter[charR]))
                
        return ans
            
            
        
        
        
